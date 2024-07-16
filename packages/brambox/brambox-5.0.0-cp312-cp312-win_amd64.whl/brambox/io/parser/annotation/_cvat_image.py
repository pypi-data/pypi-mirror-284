#
#   Copyright EAVISE
#   Author: Tanguy Ophoff
#
import xml.etree.ElementTree as ET

import pandas as pd

from brambox._imports import pgpd, shapely

from .._formats import register_parser
from .._parser import AnnotationParser, ParserType

__all__ = ['CvatImageAnnoParser']


@register_parser('cvat_image')
class CvatImageAnnoParser(AnnotationParser):
    """
    This parser can parse annotations in the `CVAT for images <cvat_>`_ format.
    This format consists of one xml file for the whole dataset.

    Args:
        extra_attributes (boolean, optional):
            Whether to parse extra attributes from the format as new columns; Default **True**
        z_order (boolean, optional):
            Whether to parse the z_order attributes of the various objects; Default **False**

    Note:
        Currently only `<box/>`, `<polygon/>`, `<points/>` and `<polyline/>` elements are parsed.

    Warning:
        Any element from the annotation format is always mapped to the standard brambox box columns: `x_top_left`, `y_top_left`, `width`, `height`.
        If you installed shapely and pgpd, more detailed shapes are available in the `segmentation` column.
    """

    parser_type = ParserType.SINGLE_FILE
    extension = '.xml'

    def __init__(self, extra_attributes=True, z_order=False):
        super().__init__()
        self.extra_attributes = extra_attributes
        self.z_order = z_order

        self.add_column('occluded', None, bool)
        if self.z_order:
            self.add_column('z_order', 0, int)
        if pgpd is not None:
            self.add_column('segmentation', pd.NA, 'geos')

    def serialize(self, df):
        raise NotImplementedError('Serialization not implemented for this parser')

    def deserialize(self, rawdata, file_id=None):
        root = ET.fromstring(rawdata)

        # Parse tasks
        task_map = {}
        tasks = find_assert(root, 'meta', 'project', 'tasks')
        for task in tasks.iter('task'):
            task_map[task.find('id').text] = task.find('name').text

        # Parse extra attributes
        attribute_types = {}
        if self.extra_attributes:
            labels = find_assert(root, 'meta', 'project', 'labels')
            for attr in labels.iter('attribute'):
                name = attr.find('name').text.lower()

                attr_type = attr.find('input_type').text.lower()
                if attr_type == 'number':
                    attribute_types[name] = int_or_float
                elif attr_type == 'checkbox':
                    attribute_types[name] = boolean
                else:
                    attribute_types[name] = string

                if name not in self.data:
                    default_value = attr.find('default_value')
                    if default_value is not None:
                        self.add_column(name, attribute_types[name](default_value.text))
                    else:
                        self.add_column(name, pd.NA)

        # Parse image annotations
        for img in root.iter('image'):
            img_name = img.get('name') or img.get('id')
            task_id = img.get('task_id')
            if task_id:
                img_name = f'{task_map[task_id]}/{img_name}'
            self.append_image(img_name)

            for box in img.findall('box'):
                self.append(**deserialize_box(img_name, box, self.z_order, self.extra_attributes, attribute_types))
            for poly in img.findall('polygon'):
                self.append(**deserialize_polygon(img_name, poly, self.z_order, self.extra_attributes, attribute_types))
            for line in img.findall('polyline'):
                self.append(**deserialize_polyline(img_name, line, self.z_order, self.extra_attributes, attribute_types))
            for points in img.findall('points'):
                self.append(**deserialize_points(img_name, points, self.z_order, self.extra_attributes, attribute_types))

    def post_deserialize(self, df):
        if 'segmentation' in df.columns:
            if df['segmentation'].isna().all():
                df = df.drop(columns=['segmentation'])
            elif df['segmentation'].isna().any():
                # Mix of polygon/points/polyline and box, but we do not compute segmentation for box
                mask = df['segmentation'].isna()
                df.loc[mask, 'segmentation'] = shapely.box(
                    df.loc[mask, 'x_top_left'].values,
                    df.loc[mask, 'y_top_left'].values,
                    df.loc[mask, 'x_top_left'].values + df.loc[mask, 'width'].values,
                    df.loc[mask, 'y_top_left'].values + df.loc[mask, 'height'].values,
                )

        return df


def deserialize_box(img_name, box, z_order, extra_attributes, attribute_types):
    xtl = float(box.get('xtl'))
    ytl = float(box.get('ytl'))
    data = {
        'image': img_name,
        'class_label': box.get('label', '').lower().strip(),
        'x_top_left': xtl,
        'y_top_left': ytl,
        'width': float(box.get('xbr')) - xtl,
        'height': float(box.get('ybr')) - ytl,
        'occluded': box.get('occluded', '0') == '1',
    }

    if z_order:
        data['z_order'] = int(box.get('z_order', 0))
    if extra_attributes:
        for attr in box.iter('attribute'):
            name = attr.get('name').lower()
            data[name] = attribute_types.get(name, string)(attr.text)

    return data


def deserialize_polygon(img_name, poly, z_order, extra_attributes, attribute_types):
    pts = [[float(c) for c in pt.split(',')] for pt in poly.get('points').split(';')]
    xs = tuple(pt[0] for pt in pts)
    ys = tuple(pt[1] for pt in pts)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    data = {
        'image': img_name,
        'class_label': poly.get('label', '').lower().strip(),
        'x_top_left': xmin,
        'y_top_left': ymin,
        'width': xmax - xmin,
        'height': ymax - ymin,
        'occluded': poly.get('occluded', '0') == '1',
    }

    if z_order:
        data['z_order'] = int(poly.get('z_order', 0))
    if extra_attributes:
        for attr in poly.iter('attribute'):
            name = attr.get('name').lower()
            data[name] = attribute_types.get(name, string)(attr.text)

    if pgpd is not None:
        data['segmentation'] = shapely.Polygon(pts)

    return data


def deserialize_polyline(img_name, line, z_order, extra_attributes, attribute_types):
    pts = [[float(c) for c in pt.split(',')] for pt in line.get('points').split(';')]
    xs = tuple(pt[0] for pt in pts)
    ys = tuple(pt[1] for pt in pts)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    data = {
        'image': img_name,
        'class_label': line.get('label', '').lower().strip(),
        'x_top_left': xmin,
        'y_top_left': ymin,
        'width': xmax - xmin,
        'height': ymax - ymin,
        'occluded': line.get('occluded', '0') == '1',
    }

    if z_order:
        data['z_order'] = int(line.get('z_order', 0))
    if extra_attributes:
        for attr in line.iter('attribute'):
            name = attr.get('name').lower()
            data[name] = attribute_types.get(name, string)(attr.text)

    if pgpd is not None:
        data['segmentation'] = shapely.LineString(pts)

    return data


def deserialize_points(img_name, points, z_order, extra_attributes, attribute_types):
    pts = [[float(c) for c in pt.split(',')] for pt in points.get('points').split(';')]
    xs = tuple(pt[0] for pt in pts)
    ys = tuple(pt[1] for pt in pts)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    data = {
        'image': img_name,
        'class_label': points.get('label', '').lower().strip(),
        'x_top_left': xmin,
        'y_top_left': ymin,
        'width': xmax - xmin,
        'height': ymax - ymin,
        'occluded': points.get('occluded', '0') == '1',
    }

    if z_order:
        data['z_order'] = int(points.get('z_order', 0))
    if extra_attributes:
        for attr in points.iter('attribute'):
            name = attr.get('name').lower()
            data[name] = attribute_types.get(name, string)(attr.text)

    if pgpd is not None:
        data['segmentation'] = shapely.MultiPoint(pts)

    return data


def find_assert(node, *keys):
    root_tag = node.tag
    for key in keys:
        node = node.find(key)
        assert node is not None, f'Node "{root_tag}" should contain {keys}, yet failed at {key}'
    return node


def int_or_float(value):
    try:
        return int(value)
    except ValueError:
        return float(value)


def boolean(value):
    if value.lower() in ('true', '1'):
        return True
    return False


def string(value):
    return value.lower().strip()

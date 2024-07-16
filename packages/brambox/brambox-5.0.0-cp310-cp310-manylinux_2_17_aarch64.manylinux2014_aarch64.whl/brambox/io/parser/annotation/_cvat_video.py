#
#   Copyright EAVISE
#   Author: Tanguy Ophoff
#
import xml.etree.ElementTree as ET

import pandas as pd

from brambox._imports import pgpd, shapely

from .._formats import register_parser
from .._parser import AnnotationParser, ParserType

__all__ = ['CvatVideoAnnoParser']


@register_parser('cvat_video')
class CvatVideoAnnoParser(AnnotationParser):
    """
    This parser can parse annotations in the `CVAT for videos <cvat_>`_ format.
    This format consists of one xml file for the whole dataset.

    Args:
        extra_attributes (boolean, optional):
            Whether to parse extra attributes from the format as new columns; Default **True**
        keyframe (boolean, optional):
            Whether to parse the keyframe boolean attribute of the various objects; Default **False**
        z_order (boolean, optional):
            Whether to parse the z_order integer attribute of the various objects; Default **False**

    Note:
        Currently only `<box/>`, `<polygon/>`, `<points/>` and `<polyline/>` elements are parsed.

    Warning:
        Any element from the annotation format is always mapped to the standard brambox box columns: `x_top_left`, `y_top_left`, `width`, `height`.
        If you installed shapely and pgpd, more detailed shapes are available in the `segmentation` column.
    """

    parser_type = ParserType.SINGLE_FILE
    extension = '.xml'

    def __init__(self, extra_attributes=True, keyframe=False, z_order=False):
        super().__init__()
        self.extra_attributes = extra_attributes
        self.keyframe = keyframe
        self.z_order = z_order

        self.add_column('id', pd.NA, pd.Int64Dtype())
        self.add_column('outside', None, bool)
        self.add_column('occluded', None, bool)
        if self.keyframe:
            self.add_column('keyframe', None, bool)
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
            name = task.find('name').text
            start = int(task.find('start_frame').text)
            stop = int(task.find('stop_frame').text)

            task_map[task.find('id').text] = name
            for i in range(start, stop + 1):
                self.append_image(f'{name}/{i:05d}')

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
        for track in root.iter('track'):
            task_name = task_map[track.get('task_id')]
            track_id = int(track.get('id'))
            track_label = track.get('label', '').lower().strip()

            for box in track.findall('box'):
                self.append(
                    id=track_id,
                    class_label=track_label,
                    **deserialize_box(task_name, box, self.keyframe, self.z_order, self.extra_attributes, attribute_types),
                )
            for poly in track.findall('polygon'):
                self.append(
                    id=track_id,
                    class_label=track_label,
                    **deserialize_polygon(task_name, poly, self.keyframe, self.z_order, self.extra_attributes, attribute_types),
                )
            for line in track.findall('polyline'):
                self.append(
                    id=track_id,
                    class_label=track_label,
                    **deserialize_polyline(task_name, line, self.keyframe, self.z_order, self.extra_attributes, attribute_types),
                )
            for points in track.findall('points'):
                self.append(
                    id=track_id,
                    class_label=track_label,
                    **deserialize_points(task_name, points, self.keyframe, self.z_order, self.extra_attributes, attribute_types),
                )

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


def deserialize_box(task_name, box, keyframe, z_order, extra_attributes, attribute_types):
    frame_idx = int(box.get('frame'))
    xtl = float(box.get('xtl'))
    ytl = float(box.get('ytl'))
    data = {
        'image': f'{task_name}/{frame_idx:05d}',
        'x_top_left': xtl,
        'y_top_left': ytl,
        'width': float(box.get('xbr')) - xtl,
        'height': float(box.get('ybr')) - ytl,
        'occluded': box.get('occluded', '0') == '1',
        'outside': box.get('outside', '0') == '1',
    }

    if keyframe:
        data['keyframe'] = box.get('keyframe', '0') == '1'
    if z_order:
        data['z_order'] = int(box.get('z_order', 0))
    if extra_attributes:
        for attr in box.iter('attribute'):
            name = attr.get('name').lower()
            data[name] = attribute_types.get(name, string)(attr.text)

    return data


def deserialize_polygon(task_name, poly, keyframe, z_order, extra_attributes, attribute_types):
    frame_idx = int(poly.get('frame'))
    pts = [[float(c) for c in pt.split(',')] for pt in poly.get('points').split(';')]
    xs = tuple(pt[0] for pt in pts)
    ys = tuple(pt[1] for pt in pts)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    data = {
        'image': f'{task_name}/{frame_idx:05d}',
        'x_top_left': xmin,
        'y_top_left': ymin,
        'width': xmax - xmin,
        'height': ymax - ymin,
        'occluded': poly.get('occluded', '0') == '1',
        'outside': poly.get('outside', '0') == '1',
    }

    if keyframe:
        data['keyframe'] = poly.get('keyframe', '0') == '1'
    if z_order:
        data['z_order'] = int(poly.get('z_order', 0))
    if extra_attributes:
        for attr in poly.iter('attribute'):
            name = attr.get('name').lower()
            data[name] = attribute_types.get(name, string)(attr.text)

    if pgpd is not None:
        data['segmentation'] = shapely.Polygon(pts)

    return data


def deserialize_polyline(task_name, line, keyframe, z_order, extra_attributes, attribute_types):
    frame_idx = int(line.get('frame'))
    pts = [[float(c) for c in pt.split(',')] for pt in line.get('points').split(';')]
    xs = tuple(pt[0] for pt in pts)
    ys = tuple(pt[1] for pt in pts)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    data = {
        'image': f'{task_name}/{frame_idx:05d}',
        'x_top_left': xmin,
        'y_top_left': ymin,
        'width': xmax - xmin,
        'height': ymax - ymin,
        'occluded': line.get('occluded', '0') == '1',
        'outside': line.get('outside', '0') == '1',
    }

    if keyframe:
        data['keyframe'] = line.get('keyframe', '0') == '1'
    if z_order:
        data['z_order'] = int(line.get('z_order', 0))
    if extra_attributes:
        for attr in line.iter('attribute'):
            name = attr.get('name').lower()
            data[name] = attribute_types.get(name, string)(attr.text)

    if pgpd is not None:
        data['segmentation'] = shapely.LineString(pts)

    return data


def deserialize_points(task_name, points, keyframe, z_order, extra_attributes, attribute_types):
    frame_idx = int(points.get('frame'))
    pts = [[float(c) for c in pt.split(',')] for pt in points.get('points').split(';')]
    xs = tuple(pt[0] for pt in pts)
    ys = tuple(pt[1] for pt in pts)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    data = {
        'image': f'{task_name}/{frame_idx:05d}',
        'x_top_left': xmin,
        'y_top_left': ymin,
        'width': xmax - xmin,
        'height': ymax - ymin,
        'occluded': points.get('occluded', '0') == '1',
        'outside': points.get('outside', '0') == '1',
    }

    if keyframe:
        data['keyframe'] = points.get('keyframe', '0') == '1'
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

#
#   Copyright EAVISE
#   Author: Tanguy Ophoff
#
import logging

import pandas as pd

from brambox._imports import pgpd

from .._formats import register_parser
from .._parser import AnnotationParser, ParserType

try:
    import yaml
except ImportError:
    yaml = None

__all__ = ['YamlParser']
log = logging.getLogger(__name__)


@register_parser('yaml')
class YamlParser(AnnotationParser):
    """
    This parser generates a lightweight human readable annotation format.
    With only one file for the entire dataset, this format will save you precious HDD space and will also be parsed faster.

    Keyword Args:
        keep_ignore (boolean): Whether are not you want to save/load the ignore value; Default **False**
        precision (integer): The number of decimals for the coordinates; Default **None** (save as int)

    Example:
        >>> annotations.yaml
            img1:
              car:
                - coords: [x,y,w,h]
                  ignore: False
              person:
                - id: 1
                  coords: [x,y,w,h]
                  ignore: True
                - id: 2
                  coords: [x,y,w,h]
                  ignore: False
            img2:
              car:
                - coords: [x,y,w,h]
                  ignore: False
    """

    parser_type = ParserType.SINGLE_FILE
    serialize_group = 'image'  # Easier to generate one string per image to add image label
    extension = '.yaml'

    def __init__(self, keep_ignore=True, precision=None):
        super().__init__()

        if yaml is None:
            raise ImportError('Pyyaml package not found. Please install it in order to use this parser!')

        self.keep_ignore = keep_ignore
        self.precision = precision
        self.add_column('id', pd.NA, pd.Int64Dtype())
        if pgpd is not None:
            self.add_column('segmentation', pd.NA, 'geos')

    def serialize(self, df):
        result = {}

        has_segmentation = 'segmentation' in df.columns and str(df['segmentation'].dtype) == 'geos'
        if has_segmentation:
            df['wkt'] = pd.NA
            df.loc[~df['segmentation'].isna(), 'wkt'] = df.loc[~df['segmentation'].isna(), 'segmentation'].geos.to_wkt()

        for row in df.itertuples():
            box = {
                'coords': [
                    round(row.x_top_left, self.precision),
                    round(row.y_top_left, self.precision),
                    round(row.width, self.precision),
                    round(row.height, self.precision),
                ],
            }
            if not pd.isna(row.id):
                box['id'] = int(row.id)
            if self.keep_ignore:
                box['ignore'] = row.ignore
            if has_segmentation and not pd.isna(row.wkt):
                box['segmentation'] = row.wkt

            class_label = row.class_label if row.class_label != '' else '?'
            if class_label not in result:
                result[class_label] = [box]
            else:
                result[class_label].append(box)

        return yaml.dump({df.name: result}, default_flow_style=None)

    def deserialize(self, rawdata, file_id=None):
        yml_obj = yaml.safe_load(rawdata)

        for file_id in yml_obj:
            self.append_image(file_id)
            if yml_obj[file_id] is not None:
                for class_label, annos in yml_obj[file_id].items():
                    for anno in annos:
                        data = {
                            'class_label': '' if class_label == '?' else class_label,
                            'x_top_left': float(anno['coords'][0]),
                            'y_top_left': float(anno['coords'][1]),
                            'width': float(anno['coords'][2]),
                            'height': float(anno['coords'][3]),
                        }

                        if 'id' in anno:
                            data['id'] = anno['id']
                        if self.keep_ignore and 'ignore' in anno:
                            data['ignore'] = anno['ignore']
                        if pgpd is not None and 'segmentation' in anno:
                            data['segmentation'] = pd.NA if anno['segmentation'] == 'null' else anno['segmentation']

                        self.append(file_id, **data)

    def post_deserialize(self, df):
        if df['id'].isna().all():
            df = df.drop(columns=['id'])

        if 'segmentation' in df.columns and df['segmentation'].isna().all():
            df = df.drop(columns='segmentation')

        return df

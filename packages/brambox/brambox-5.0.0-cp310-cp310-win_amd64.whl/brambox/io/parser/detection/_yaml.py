#
#   Copyright EAVISE
#   Author: Tanguy Ophoff
#
import logging

import pandas as pd

from brambox._imports import pgpd

from .._formats import register_parser
from .._parser import DetectionParser, ParserType

try:
    import yaml
except ImportError:
    yaml = None

__all__ = ['YamlParser']
log = logging.getLogger(__name__)


@register_parser('yaml')
class YamlParser(DetectionParser):
    """
    This parser generates a lightweight human readable detection format.
    With only one file for the entire dataset, this format will save you precious HDD space and will also be parsed faster.

    Keyword Args:
        precision (integer): The number of decimals for the coordinates; Default **None** (save as int)

    Example:
        >>> detections.yaml
            img1:
              car:
                - coords: [x,y,w,h]
                  score: 56.76
              person:
                - coords: [x,y,w,h]
                  id: 1
                  score: 90.1294132
                - coords: [x,y,w,h]
                  id: 2
                  score: 12.120
            img2:
              car:
                - coords: [x,y,w,h]
                  score: 50
    """

    parser_type = ParserType.SINGLE_FILE
    serialize_group = 'image'
    extension = '.yaml'

    def __init__(self, precision=None):
        super().__init__()

        if yaml is None:
            raise ImportError('Pyyaml package not found. Please install it in order to use this parser!')

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
                'score': row.confidence * 100,
            }

            if not pd.isna(row.id):
                box['id'] = int(row.id)
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
            if yml_obj is not None:
                for class_label, dets in yml_obj[file_id].items():
                    for det in dets:
                        data = {
                            'class_label': '' if class_label == '?' else class_label,
                            'x_top_left': float(det['coords'][0]),
                            'y_top_left': (det['coords'][1]),
                            'width': float(det['coords'][2]),
                            'height': float(det['coords'][3]),
                            'confidence': det['score'] / 100,
                        }

                        if 'id' in det:
                            data['id'] = det['id']
                        if pgpd is not None and 'segmentation' in det:
                            data['segmentation'] = pd.NA if det['segmentation'] == 'null' else det['segmentation']

                        self.append(file_id, **data)

    def post_deserialize(self, df):
        if df['id'].isna().all():
            df = df.drop(columns=['id'])

        if 'segmentation' in df.columns and df['segmentation'].isna().all():
            df = df.drop(columns=['segmentation'])

        return df

#
#   Copyright EAVISE
#   Author: Tanguy Ophoff
#
import logging
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd

from brambox._imports import pgpd, shapely

from .._formats import register_parser
from .._parser import AnnotationParser, ParserType

__all__ = ['HRSCParser']
log = logging.getLogger(__name__)


@register_parser('hrsc')
class HRSCParser(AnnotationParser):
    """
    This parser can parse annotations in the `HRSC 2016 <hrsc_>`_ format.
    This format consists of one xml file for every image.

    Example:
        >>> image_100000001.xml
            <HRSC_Image>
              <Img_ID>100000001</Img_ID>
              <Place_ID>100000001</Place_ID>
              <Source_ID>100000001</Source_ID>
              <Img_NO>100000001</Img_NO>
              <Img_FileName>100000001</Img_FileName>
              <Img_FileFmt>bmp</Img_FileFmt>
              <Img_Date>2014-07-01</Img_Date>
              <Img_CusType>sealand</Img_CusType>
              <Img_Des></Img_Des>
              <Img_Location>69.040297,33.070036</Img_Location>
              <Img_SizeWidth>1166</Img_SizeWidth>
              <Img_SizeHeight>753</Img_SizeHeight>
              <Img_SizeDepth>3</Img_SizeDepth>
              <Img_Resolution>1.07</Img_Resolution>
              <Img_Resolution_Layer>18</Img_Resolution_Layer>
              <Img_Scale>100</Img_Scale>
              <Img_SclPxlNum></Img_SclPxlNum>
              <segmented>0</segmented>
              <Img_Havemask>0</Img_Havemask>
              <Img_MaskFileName></Img_MaskFileName>
              <Img_MaskFileFmt></Img_MaskFileFmt>
              <Img_MaskType></Img_MaskType>
              <Img_SegFileName></Img_SegFileName>
              <Img_SegFileFmt></Img_SegFileFmt>
              <Img_Rotation>090d</Img_Rotation>
              <Annotated>1</Annotated>
              <HRSC_Objects>
                <HRSC_Object>
                  <Object_ID>100000001</Object_ID>
                  <Class_ID>100000013</Class_ID>
                  <Object_NO>100000001</Object_NO>
                  <truncated>0</truncated>
                  <difficult>0</difficult>
                  <box_xmin>194</box_xmin>
                  <box_ymin>243</box_ymin>
                  <box_xmax>972</box_xmax>
                  <box_ymax>507</box_ymax>
                  <mbox_cx>582.9349</mbox_cx>
                  <mbox_cy>353.2006</mbox_cy>
                  <mbox_w>778.1303</mbox_w>
                  <mbox_h>174.2541</mbox_h>
                  <mbox_ang>-0.2144308</mbox_ang>
                  <segmented>0</segmented>
                  <seg_color></seg_color>
                  <header_x>964</header_x>
                  <header_y>290</header_y>
                </HRSC_Object>
              </HRSC_Objects>
            </HRSC_Image>
    """

    parser_type = ParserType.MULTI_FILE
    serialize_group = 'image'
    extension = '.xml'

    def __init__(self, extract_oriented=True):
        super().__init__()
        self.add_column('truncated', 0, float)
        self.add_column('difficult', False, bool)

        self.extract_oriented = extract_oriented
        if self.extract_oriented:
            if pgpd is None:
                raise ImportError('The HRSC parser requires shapely and pgpd to be installed, if you want oriented data!')
            self.add_column('segmentation', pd.NA, 'geos')

    def serialize(self, df):
        raise NotImplementedError('Serialization not implemented for this parser')

    def deserialize(self, rawdata, file_id=None):
        self.append_image(file_id)

        root = ET.fromstring(rawdata)
        for xml_obj in root.iter('HRSC_Object'):
            x_top_left = float(xml_obj.findtext('box_xmin', 0))
            y_top_left = float(xml_obj.findtext('box_ymin', 0))
            width = float(xml_obj.findtext('box_xmax', 0)) - x_top_left
            height = float(xml_obj.findtext('box_ymax', 0)) - y_top_left

            extra = {}
            if self.extract_oriented:
                obb_cx = float(xml_obj.findtext('mbox_cx', 0))
                obb_cy = float(xml_obj.findtext('mbox_cy', 0))
                obb_w = float(xml_obj.findtext('mbox_w', 0))
                obb_h = float(xml_obj.findtext('mbox_h', 0))
                obb_a = float(xml_obj.findtext('mbox_ang', 0))
                cos, sin = np.cos(obb_a), np.sin(obb_a)
                center = np.array([obb_cx, obb_cy])
                vec1 = np.array([obb_w / 2 * cos, obb_w / 2 * sin])
                vec2 = np.array([-obb_h / 2 * sin, obb_h / 2 * cos])
                point1 = center - vec1 - vec2
                point2 = center + vec1 - vec2
                point3 = center + vec1 + vec2
                point4 = center - vec1 + vec2
                extra['segmentation'] = shapely.polygons(np.stack([point1, point2, point3, point4]))

            self.append(
                file_id,
                class_label=xml_obj.findtext('Class_ID', ''),
                x_top_left=x_top_left,
                y_top_left=y_top_left,
                width=width,
                height=height,
                truncated=float(xml_obj.findtext('truncated', 0)),
                difficult=xml_obj.findtext('difficult', 0) == '1',
                **extra,
            )

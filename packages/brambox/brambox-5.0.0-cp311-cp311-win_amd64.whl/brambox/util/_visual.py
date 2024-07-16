#
#   Copyright EAVISE
#   Author: Tanguy Ophoff
#   Visualization functionality
#
import logging
from collections.abc import Sequence
from enum import Enum
from pathlib import Path

import numpy as np
import pandas as pd

from brambox._imports import shapely

log = logging.getLogger(__name__)  # noqa
default = None  # noqa

try:
    import cv2

    default = 0
except ModuleNotFoundError:
    log.debug('OpenCV not installed')
    cv2 = None

try:
    from PIL import Image, ImageColor, ImageDraw, ImageFont

    default = 1

    try:
        font = ImageFont.truetype('DejaVuSansMono', 10)
    except IOError:
        font = ImageFont.load_default()
except ModuleNotFoundError:
    log.debug('Pillow not installed')
    Image = None

if Image is None and cv2 is None:
    log.error('Neither Pillow nor OpenCV installed, visualization functions will not work')


__all__ = ['BoxDrawer', 'draw_boxes', 'DrawMethod']


class DrawMethod(Enum):
    """Which library to use for drawing"""

    CV = 0 if cv2 is not None else None  #: Use OpenCV
    PIL = 1 if Image is not None else None  #: Use Pillow


def draw_boxes(img, boxes, label=False, color=None, size=3, alpha=1, method=default):
    """Draws bounding boxes on an image. |br|
    If the boxes dataframe contains a segmentation column, a polygon is drawn.
    Otherwise we draw a horizontal bounding box.

    Args:
        img (OpenCV image or PIL image or filename):
            Image to draw on
        boxes (pandas.DataFrame):
            Bounding boxes to draw
        label (pandas.Series, optional):
            Label to write above the boxes; Default **nothing**
        color (pandas.Series, optional):
            Color to use for drawing; Default **every class_label will get its own color, up to 10 labels**
        size (pandas.Series, optional):
            Thickness of the border of the bounding boxes (set to -1 for fill); Default **3**
        alpha (pandas.Series, optional):
            Alpha value for the border or fill; Default **1**
        method (DrawMethod, optional):
            Whether to use OpenCV or Pillow for opening the image (only useful when filename given); Default: **DrawMethod.PIL**

    Returns:
        OpenCV or PIL image: Image with bounding boxes drawn

    Note:
        The `label`, `color`, `size` and `alpha` arguments can also be tacked on to the `boxes` dataframe as columns.
        They can also be a single value, which will then be used for each bounding box. |br|
        Basically, as long as you can assign the value as a new column to the dataframe, it will work.

    Note:
        The default drawing method depends on whichever library is installed (cv2 or PIL)
        and is only used if the image passed is a string or Path object.
        If both are installed, Pillow is the default choice.
    """
    if DrawMethod(method).value is None:
        raise ImportError(f'Could not find the correct library for the chosen drawing method [{DrawMethod(method)}]')

    # Open image
    if isinstance(img, (str, Path)):
        if method == DrawMethod.CV:
            img = cv2.imread(img)
        else:
            method = DrawMethod.PIL
            original = Image.open(img)
            if original.mode == 'L':
                original = original.convert('RGB')
            img = ImageDraw.Draw(original, 'RGBA')
    elif Image is not None and isinstance(img, Image.Image):
        img = img.copy()
        original = img.convert('RGB') if img.mode == 'L' else img
        img = ImageDraw.Draw(original, 'RGBA')
        method = DrawMethod.PIL
    elif cv2 is not None and isinstance(img, np.ndarray):
        img = img.copy()
        method = DrawMethod.CV
    else:
        raise TypeError(f'Unkown image type [{type(img)}]')

    # Draw
    draw = draw_cv if method == DrawMethod.CV else draw_pil
    if not boxes.empty:
        boxes = setup_boxes(boxes, label, color, size, alpha)
        for box in boxes.itertuples():
            draw(img, box)

    if method == DrawMethod.PIL:
        return original
    return img


class BoxDrawer:
    """This class allows to iterate over all images in a dataset and draw their respective bounding boxes.

    Args:
        images (callable or dict-like object):
            A way to get the image or path to the image from the image labels in the dataframe
        boxes (pandas.DataFrame):
            Bounding boxes to draw
        label (pandas.Series, optional):
            Label to write above the boxes; Default **nothing**
        color (pandas.Series, optional):
            Color to use for drawing; Default **every class_label will get its own color, up to 10 labels**
        size (pandas.Series, optional):
            Thickness of the border of the bounding boxes (set to -1 for fill); Default **3**
        alpha (pandas.Series, optional):
            Alpha value for the border or fill; Default **1**
        show_empty (boolean, optional):
            Whether to also show images without bounding boxes; Default **True**
        method (DrawMethod, optional):
            Whether to use OpenCV or Pillow for opening the image (only useful when filename given); Default: **DrawMethod.PIL**

    Note:
        If the `images` argument is callable, the image or path to the image will be retrieved in the following way:

        >>> image = self.images(image_label)

        Otherwise the image or path is retrieved as:

        >>> image = self.images[image_label]

    Note:
        The `label`, `color`, `size`, `alpha` and `fill` arguments can also be tacked on to the `boxes` dataframe as columns.
        They can also be a single value, which will then be used for each bounding box. |br|
        Basically, as long as you can assign the value as a new column to the dataframe, it will work.

    Note:
        The default drawing method depends on whichever library is installed (cv2 or PIL)
        and is only used if the images passed are string or Path objects.
        If both are installed, Pillow is the default choice.
    """

    def __init__(self, images, boxes, label=False, color=None, size=3, alpha=1, show_empty=True, method=default):
        self.images = images
        self.boxes = setup_boxes(boxes, label, color, size, alpha)

        self.method = method
        if DrawMethod(self.method).value is None:
            raise ImportError(f'Could not find the correct library for the chosen drawing method [{DrawMethod(method)}]')

        if show_empty:
            self.image_labels = list(self.boxes.image.cat.categories)
        else:
            self.image_labels = list(self.boxes.image.cat.remove_unused_categories().cat.categories)

    def __len__(self):
        return len(self.image_labels)

    def __getitem__(self, idx):
        """Get image with boxes drawn onto it.

        Args:
            idx (str or int): Numerical index or image string

        Returns:
            OpenCV or PIL image: Image with bounding boxes drawn
        """
        lbl = self.image_labels[idx] if isinstance(idx, int) else idx
        img = self.images(lbl) if callable(self.images) else self.images[lbl]
        return self.draw(lbl, img, self.boxes[self.boxes.image == lbl])

    def draw(self, lbl, img, boxes):
        if isinstance(img, (str, Path)):
            if self.method == DrawMethod.CV:
                img = cv2.imread(img)
                method = DrawMethod.CV
            else:
                original = Image.open(img)
                if original.mode == 'L':
                    original = original.convert('RGB')
                img = ImageDraw.Draw(original, 'RGBA')
                method = DrawMethod.PIL
        elif Image is not None and isinstance(img, Image.Image):
            original = img.convert('RGB') if img.mode == 'L' else img
            img = ImageDraw.Draw(original, 'RGBA')
            method = DrawMethod.PIL
        elif cv2 is not None and isinstance(img, np.ndarray):
            method = DrawMethod.CV
        else:
            raise TypeError(f'Unkown image type [{type(img)}]')

        # Draw
        draw = draw_cv if method == DrawMethod.CV else draw_pil
        if not boxes.empty:
            for box in boxes.itertuples():
                draw(img, box)

        if method == DrawMethod.PIL:
            return original
        return img


def setup_boxes(boxes, label=False, color=None, size=3, alpha=1):
    """Setup the boxes dataframe with the correct metadata columns to draw them.
    This function basically adds on 3 columns ['label', 'color', 'size'] if they are not yet on the dataframe.

    Args:
        boxes (pandas.DataFrame):
            Bounding boxes to draw
        label (pandas.Series, optional):
            Label to write above the boxes; Default **nothing**
        color (pandas.Series, optional):
            Color to use for drawing; Default **every class_label will get its own color, up to 10 labels**
        size (pandas.Series, optional):
            Thickness of the border of the bounding boxes; Default **3**
        alpha (pandas.Series, optional):
            Alpha value for the border or fill if enabled; Default **1**
        fill (pandas.Series, optional):
            Whether to fill the boxes or not; Default **False**

    Returns:
        pandas.DataFrame:
            brambox dataframe with 6 extra columns ['points', 'label', 'color', 'size', 'alpha', 'fill']
    """
    default_colors = [
        (31, 119, 180),
        (255, 127, 14),
        (44, 160, 44),
        (214, 39, 40),
        (148, 103, 189),
        (140, 86, 75),
        (227, 119, 194),
        (127, 127, 127),
        (188, 189, 34),
        (23, 190, 207),
    ]
    boxes = boxes.copy()

    # Filter NaN and Inf coordinates
    coords = ['x_top_left', 'y_top_left', 'width', 'height']
    isinf = np.any(np.isinf(boxes[coords]))
    isna = pd.isna(boxes[coords]).any(axis=None)

    if isinf:
        log.error('Some bounding boxes contain Inf coordinates')
        boxes[coords] = boxes[coords].replace((np.inf, -np.inf), np.nan)
    if isna:
        log.error('Some bounding boxes contain NaN coordinates')
    if isinf or isna:
        boxes = boxes.dropna(subset=coords)

    # Setup color
    if 'color' not in boxes.columns:
        if color is not None:
            # Check if color is a single RGB sequence
            if isinstance(color, Sequence) and len(color) == 3 and isinstance(color[0], int):
                boxes['color'] = [color] * len(boxes)
            else:
                boxes['color'] = color
        else:
            labels = sorted(boxes.class_label.unique())
            boxes['color'] = boxes.class_label.map({v: i for i, v in enumerate(labels)})

    # If color column is integer, we assume user wants to map it to default color list
    if pd.api.types.is_integer_dtype(boxes['color']):
        boxes['color'] %= len(default_colors)
        boxes['color'] = boxes['color'].map(dict(enumerate(default_colors)))

    # Setup border width
    if 'size' not in boxes.columns:
        boxes['size'] = size
        boxes['size'] = boxes['size'].astype(int)

    # Setup label
    if 'label' not in boxes.columns:
        if label is True:
            boxes['label'] = boxes['class_label']
            if 'id' in boxes.columns:
                boxes['label'] += boxes.apply(lambda b: f' {b.id}' if not pd.isna(b.id) else '', axis=1)
            if 'confidence' in boxes.columns:
                boxes.label += ' [' + (boxes.confidence * 100).round(2).astype(str) + '%]'
        else:
            boxes['label'] = label

    # Setup alpha
    if 'alpha' not in boxes.columns:
        boxes['alpha'] = alpha
        boxes['alpha'] = boxes['alpha'].astype(float)

    # Setup box points
    if 'angle' in boxes.columns:
        w, h, a = boxes['width'].to_numpy(), boxes['height'].to_numpy(), boxes['angle'].to_numpy()
        side1 = np.stack((w * np.cos(a), -w * np.sin(a)), -1)
        side2 = np.stack((h * np.sin(a), h * np.cos(a)), -1)

        tl = boxes[['x_top_left', 'y_top_left']].to_numpy()
        tr = tl + side1
        br = tr + side2
        bl = br - side1
        boxes['points'] = np.array((tl, tr, br, bl, tl)).swapaxes(0, 1).astype(int).tolist()
        boxes['points'] = boxes['points'].apply(lambda pts: [tuple(p) for p in pts])
    else:
        x0 = boxes['x_top_left'].astype(int)
        y0 = boxes['y_top_left'].astype(int)
        x1 = (boxes['x_top_left'] + boxes['width']).astype(int)
        y1 = (boxes['y_top_left'] + boxes['height']).astype(int)

        points = pd.DataFrame(
            {
                'pt1': x0.combine(y0, lambda x, y: (x, y)),
                'pt2': x1.combine(y0, lambda x, y: (x, y)),
                'pt3': x1.combine(y1, lambda x, y: (x, y)),
                'pt4': x0.combine(y1, lambda x, y: (x, y)),
            }
        )
        points['pt5'] = points['pt1']
        boxes['points'] = points.apply(tuple, axis=1)

    return boxes


def draw_pil(img, box):
    """Draw a bounding box on a Pillow image"""
    alpha = int(box.alpha * 255)
    if isinstance(box.color, str):
        color = ImageColor.getrgb(box.color)
        if len(color) == 3:
            color = (*color, alpha)
        else:
            color[4] = alpha
    else:
        color = (*box.color[:3], alpha)

    drawn = False
    if hasattr(box, 'segmentation') and shapely is not None and not shapely.is_empty(box.segmentation):
        if isinstance(box.segmentation, shapely.Polygon):
            drawn = True
            points = [tuple(pt) for pt in shapely.get_coordinates(box.segmentation)]
            labelpt = points[0]
            if box.size < 0:
                img.polygon(points, color)
            else:
                img.line(points, color, box.size)
        elif isinstance(box.segmentation, shapely.LineString):
            drawn = True
            points = [tuple(pt) for pt in shapely.get_coordinates(box.segmentation)]
            labelpt = points[0]
            img.line(points, color, max(0, box.size))
        elif isinstance(box.segmentation, (shapely.MultiPoint, shapely.Point)):
            drawn = True
            points = [tuple(pt) for pt in shapely.get_coordinates(box.segmentation)]
            labelpt = points[0]
            size = max(0, box.size) / 2
            for pt in points:
                img.ellipse([(pt[0] - size, pt[1] - size), (pt[0] + size, pt[1] + size)], fill=color)

    if not drawn:
        labelpt = box.points[0]
        if box.size < 0:
            img.polygon(box.points, color)
        else:
            img.line(box.points, color, box.size)

    if box.label:
        labelpt = [min(max(c, 0), imgd) for c, imgd in zip(labelpt, img.im.size)]
        offset = 12 + box.size
        img.text((labelpt[0], labelpt[1] - offset), box.label, (*color[:3], 255), font)


def draw_cv(img, box):
    """Draw a bounding box on an OpenCV image"""
    if not isinstance(box.color, Sequence):
        raise ValueError('Color should be an RGB tuple')
    color = box.color[::-1]

    if box.alpha != 1:
        color = (*color, int(box.alpha * 255))
        original = np.zeros_like(img, shape=(*img.shape[:-1], 4))
        img, original = original, img

    drawn = False
    if hasattr(box, 'segmentation') and shapely is not None and not shapely.is_empty(box.segmentation):
        if isinstance(box.segmentation, shapely.Polygon):
            drawn = True
            points = shapely.get_coordinates(box.segmentation).astype(int)
            labelpt = points[0]
            if box.size < 0:
                cv2.fillPoly(img, [points], color)
            else:
                cv2.polylines(img, [points], False, color, box.size)
        elif isinstance(box.segmentation, shapely.LineString):
            drawn = True
            points = shapely.get_coordinates(box.segmentation).astype(int)
            labelpt = points[0]
            cv2.polylines(img, [points], False, color, max(0, box.size))
        elif isinstance(box.segmentation, (shapely.MultiPoint, shapely.Point)):
            drawn = True
            points = shapely.get_coordinates(box.segmentation).astype(int)
            labelpt = points[0]
            size = max(0, box.size)
            for pt in points:
                cv2.circle(img, pt, size, color, thickness=-1)

    if not drawn:
        pts = np.array(box.points, dtype=np.int32).reshape(-1, 2)
        labelpt = pts[0]
        if box.size < 0:
            cv2.fillPoly(img, [pts], color)
        else:
            cv2.polylines(img, [pts], False, color, box.size)

    if box.alpha != 1:
        alpha = img[..., -1:] / 255
        img = alpha * img[..., :3] + (1 - alpha) * original
        original[...] = img
        img = original

    if box.label:
        labelpt = [min(max(c, 0), imgd) for c, imgd in zip(labelpt, img.shape[1::-1])]
        cv2.putText(img, box.label, (labelpt[0], labelpt[1] - 5), cv2.FONT_HERSHEY_PLAIN, 0.75, color, 1, cv2.LINE_AA)

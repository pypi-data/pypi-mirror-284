#
#   Copyright EAVISE
#   File Parsers
#
__all__ = ['formats', 'register_parser', 'AnnotationParser', 'DetectionParser', 'Parser', 'ParserType']

from . import annotation, detection, generic
from ._formats import formats, register_parser
from ._parser import AnnotationParser, DetectionParser, Parser, ParserType

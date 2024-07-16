#
#   Copyright EAVISE
#   Author: Tanguy Ophoff
#
import logging

from ._parser import AnnotationParser, DetectionParser, Parser

__all__ = ['formats', 'register_parser']
log = logging.getLogger(__name__)


formats = {}


def register_parser(name, parser=None):
    """
    Registers a parser class so that any function that works with brambox parsers, can use this parser as well.

    Args:
        name (str): Key for the parser in the different dictionaries
        parser (brambox.io.parser.Parser): Parser class to register

    Note:
        If your parser is of the type :class:`~brambox.io.parser.annotation.AnnotationParser`,
        it will be registered in :ref:`formats <brambox.io.formats>` with `'anno_'+name` as the key.

        If it is of the type :class:`~brambox.io.parser.detection.DetectionParser`,
        it will be registered in :ref:`formats <brambox.io.formats>` with `'det_'+name` as the key.

        Finally, if it is neither one of those, but just of type :class:`~brambox.io.parser.Parser`,
        it will be registered in :ref:`formats <brambox.io.formats>` with `name` as the key.

    Warning:
        You cannot register a parser if that name is already taken!

    Examples:
        This function can either be used as a regular function or as a decorator.

        >>> import brambox as bb
        >>> @bb.io.register_parser('dummy')
        ... class DummyAnnoParser(bb.io.parser.AnnotationParser):
        ...     pass

        >>> import brambox as bb
        >>> class DummyDetParser(bb.io.parser.DetectionParser):
        ...     pass
        >>> bb.io.register_parser('dummy', DummyDetParser)
    """

    def _register_parser(parser):
        nonlocal name

        if not issubclass(parser, Parser):
            raise TypeError(f'{parser.__name__} is not of type {Parser}')

        if issubclass(parser, AnnotationParser):
            name = 'anno_' + name
        elif issubclass(parser, DetectionParser):
            name = 'det_' + name

        if name in formats:
            raise KeyError(f'{name} already registered for parser: {formats[name]}')
        formats[name] = parser

        return parser

    if parser is None:
        return _register_parser
    return _register_parser(parser)

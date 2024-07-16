#
#   Brambox optional dependencies
#   Copyright EAVISE
#
import logging

__all__ = [
    'pgpd',
    'shapely',
]
log = logging.getLogger(__name__)

try:
    import pgpd
    import shapely
except ModuleNotFoundError:
    log.debug('pgpd is not installed and thus segmentation related functionality will not work')
    pgpd = None
    shapely = None

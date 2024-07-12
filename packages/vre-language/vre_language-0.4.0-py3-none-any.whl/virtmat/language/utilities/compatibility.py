"""define/check grammar and data schema versions compatible to the interpreter"""
import re
from virtmat.language.utilities.logging import get_logger

versions = {'grammar': [5, 6, 7, 8, 9], 'data_schema': [3]}


class CompatibilityError(Exception):
    """raise this exception if the grammar or data schema are incompatible"""


def check_compatibility(grammar_str, data_schema=None):
    """extract the version number from the grammar"""
    logger = get_logger(__name__)
    regex = re.compile(r'\/\*\s*grammar version\s+(\d+)\s*\*\/', re.MULTILINE)
    match = re.search(regex, grammar_str)
    if match:
        logger.debug('found grammar version')
        version = int(match.group(1))
        if version not in versions['grammar']:
            msg = (f"Provided grammar has version {version} but the supported "
                   f"versions are {versions['grammar']}")
            logger.error(msg)
            raise CompatibilityError(msg)
    else:
        raise ValueError('cannot find version tag in grammar')
    if data_schema is not None:
        logger.debug('checking the schema')
        if data_schema not in versions['data_schema']:
            msg = f'Data schema version {data_schema} is not supported'
            logger.error(msg)
            raise CompatibilityError(msg)

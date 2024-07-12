""" i/o operations """
import pathlib
from urllib.request import urlopen
# from urllib import request, parse
import yaml
from fireworks.utilities.fw_serializers import load_object, recursive_dict
from virtmat.language.utilities.serializable import get_serializable
from virtmat.language.utilities.types import typemap, checktype_
from virtmat.language.utilities.errors import RuntimeTypeError


def load_value(url=None, filename=None, typ=None):
    """load data from file or from URL using the GET method"""
    assert url or filename, 'either filename or url must be specified'
    if filename:
        with open(filename, 'r', encoding='utf-8') as inp:
            val = yaml.safe_load(inp)
    elif url:
        with urlopen(url) as inp:
            val = yaml.safe_load(inp)
    if isinstance(val, dict):
        val = load_object(val)
    if typ:
        checktype_(val, typ)
    return val


def store_value(val, url=None, filename=None):
    """store data to a new file or to an URL using the POST method"""
    assert url or filename, 'either filename or url must be specified'
    if filename:
        if pathlib.Path(filename).suffix in ('.yml', '.yaml'):
            with open(filename, 'x', encoding='utf-8') as out:
                yaml.safe_dump(recursive_dict(get_serializable(val)), out)
        elif isinstance(val, typemap['AMMLStructure']):
            val.to_ase_file(filename)
        else:
            msg = f'unknown format {filename} or data type {type(val)}'
            raise RuntimeTypeError(msg)
    elif url:
        raise NotImplementedError
        # data = parse.urlencode(val).encode()
        # req =  request.Request(url, data=data)
        # resp = request.urlopen(req)

from lynx import encoder
from lynx import decoder
from lynx.format import *


__version__ = '0.3'
__all__ = [
    'load', 'loads', 'dump', 'dumps', 'Section'
]

def load(fp):
    """
    Deserialize the file as lynx format.
    Returns list of sections.
    """
    return loads(fp.read())

def loads(str):
    """
    Deserialize string as lynx format.
    Returns list of sections.
    """
    return decoder.Decoder().decode(str)


def dump(fp, section):
    """
    Serialize Section or Sections list into fp.
    """
    fp.write(encoder.encode(section))


def dumps(section):
    """
    Serialize section or sections list and returns as string.
    """
    return encoder.encode(section)





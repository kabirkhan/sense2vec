# coding: utf8
from __future__ import unicode_literals

from os import path

from .vectors import VectorMap
from .about import __version__


def load(vectors_path):
    if not path.exists(vectors_path):
        raise IOError("Can't find data directory: {}".format(vectors_path))
    vector_map = VectorMap(128)
    vector_map.load(vectors_path)
    return vector_map




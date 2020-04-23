#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.escape import to_unicode
from tornado.util import ObjectDict


def format_unicode(obj):
    # basestring
    if isinstance(obj, (str, bytes)):
        return to_unicode(obj)

    # list
    if isinstance(obj, list) or isinstance(obj, map):
        return [format_unicode(o) for o in obj]

    # dict
    if isinstance(obj, dict):
        new = ObjectDict()
        for key in obj:
            value = obj[key]
            new[key] = format_unicode(value)
        return new

    return obj


def to_bytes(string):
    if isinstance(string, str):
        return string.encode('utf-8')
    return string

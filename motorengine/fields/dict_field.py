#!/usr/bin/env python
# -*- coding: utf-8 -*-

from motorengine.fields.base_field import BaseField


class DictField(BaseField):
    '''
    Field responsible for storing dict values (:py:func:`dict`).

    Usage:

    .. testcode:: modeling_fields

        someAttibute = DictField(required=True)

    `DictField` has no additional arguments available (apart from those in `BaseField`).
    '''
    def __init__(self, *args, **kw):
        super(DictField, self).__init__(*args, **kw)

    def to_son(self, value):
        return dict(value)

    def from_son(self, value):
        return value

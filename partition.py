#!/usr/bin/env python
# -*- coding: utf-8 -*-


def partition(origin, num):
    return [origin[i:i + num] for i in range(0, len(origin), num)]

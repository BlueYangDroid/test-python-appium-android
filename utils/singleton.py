#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import functools


def singleton(cls):
    instances = {}
    functools.wraps(cls)

    def getInstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getInstance

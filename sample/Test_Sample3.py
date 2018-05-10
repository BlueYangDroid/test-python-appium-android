#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest

from sample.Test_Sample0 import TestSample0


class TestSample3(TestSample0):

    # def test_answer1(self, fixtrue_env):
    #     print('test_answer2.1: get fixtrue_env %s' % fixtrue_env)
    #     assert fixtrue_env == 10
    #
    # def test_answer_2(self, fixtrue_env):
    #     print('test_answer2.2: get fixtrue_env %s' % fixtrue_env)
    #     assert fixtrue_env == 10

    def test_answer_3(self, fixtrue_env):
        print('test_answer3: --')
        assert fixtrue_env == 10

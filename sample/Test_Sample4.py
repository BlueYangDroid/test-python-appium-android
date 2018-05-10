#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest
from sample.Test_Sample0 import TestSample0

@pytest.mark.usefixtures("fixtrue_env")
class TestSample4(TestSample0):

    def test_answer1(self, fixtrue_env):
        print('test_answer4.1: get fixtrue_env %s' % fixtrue_env)
        assert fixtrue_env == 10

    def test_answer_2(self, fixtrue_env):
        print('test_answer4.2: get fixtrue_env %s' % fixtrue_env)
        assert fixtrue_env == 10


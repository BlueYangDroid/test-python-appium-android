#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest

class TestSample0():

    @pytest.fixture(scope="session")
    def fixtrue_env(self):
        print('--> base0: setup fixtrue_env')
        yield 10
        print('<-- base0: teardown fixtrue_env')

    # def test_answer1(self, fixtrue_env):
    #     print('test_answer2.1: get fixtrue_env %s' % fixtrue_env)
    #     assert fixtrue_env == 10
    #
    # def test_answer_2(self, fixtrue_env):
    #     print('test_answer2.2: get fixtrue_env %s' % fixtrue_env)
    #     assert fixtrue_env == 10


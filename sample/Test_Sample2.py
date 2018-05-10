#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest
from sample.Test_Base import TestBase as testbase
from common.BaseElementEnmu import Action
from common.BaseElementEnmu import Option
from page.pages import *

@pytest.mark.usefixtures("fixtrue_env")
class TestSample2(testbase):

    # def test_answer1(self, fixtrue_env):
    #     print('test_answer2.1: get fixtrue_env %s' % fixtrue_env)
    #     assert fixtrue_env == 10
    #
    # def test_answer_2(self, fixtrue_env):
    #     print('test_answer2.2: get fixtrue_env %s' % fixtrue_env)
    #     assert fixtrue_env == 10

    def test_login(self):
        print('test_login: --')
        self.operater.operate(HomePageToSign.step_登录按钮, self.deviceName)
        self.operater.operate(LoginPage.step_账户, self.deviceName)
        self.operater.operate(LoginPage.step_密码, self.deviceName)
        self.operater.operate(LoginPage.step_登录, self.deviceName)
        self.operater.operate(HomePageSigned.step_登录断言, self.deviceName)

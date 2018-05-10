#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest
from testcase.TestBase import TestBase as testbase
from page.pages import *
from utils.pylog import Log as L
from arch import adb

TAG = 'TestLoginPage'

@pytest.mark.usefixtures("fixtrue_env")
class TestLoginPage(testbase):

    # def test_answer1(self, fixtrue_env):
    #     print('test_answer2.1: get fixtrue_env %s' % fixtrue_env)
    #     assert fixtrue_env == 10
    #
    # def test_answer_2(self, fixtrue_env):
    #     print('test_answer2.2: get fixtrue_env %s' % fixtrue_env)
    #     assert fixtrue_env == 10

    def test_login(self):
        L.i('\n =========> test_login', tag=TAG)
        adb.create_logcat('test_login')
        self.operater.launch(PlayStartFullscreen.step_启动首页)
        self.operater.operate(HomePageToSign.step_登录按钮, self.deviceName)
        self.operater.operate(LoginPage.step_账户, self.deviceName)
        self.operater.operate(LoginPage.step_密码, self.deviceName)
        self.operater.operate(LoginPage.step_登录, self.deviceName)
        self.operater.base_assert(HomePageSigned.step_登录断言)
        adb.stop_logcat()
        L.i(' <========= test_login\n', tag=TAG)

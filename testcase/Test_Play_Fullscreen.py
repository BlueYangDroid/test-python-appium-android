#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest

from page.pages import *
from testcase.TestBase import TestBase
from arch import tools
from utils.pylog import Log as L

TAG = 'Test_Play_Fullscreen'

@pytest.mark.usefixtures("fixtrue_env")
class TestPlayFullscreen(TestBase):

    def test_enter_auto_page(self):
        L.i('\n =========> test_enter_auto_page, device: ' + self.deviceName, tag=TAG)

        '''
        操作元素.operateInfo是字典
        find_type: find类型
        operate_type：对应的操作
        element_info：元素详情
        testInfo: 用例介绍
        logTest: 记录日志
        device: 设备名
        code: 按键
        '''
        # xpath：
        # self.driver.find_element_by_xpath(
        #     "//android.widget.ListView/android.widget.TextView[contains(@text, '自动化测试')]").click()
        # uiautomator - UiSelector：
        # name方式在1.5版本后已废除，能找到接口，不可使用，使用new UiSelector().text替代
        # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"海信广告测试\")").click()
        self.operater.launch(PlayStartFullscreen.step_启动首页)
        self.operater.operate(PlayStartFullscreen.step_进入自动化测试页, self.deviceName)
        self.operater.base_assert(PlayStartFullscreen.step_测试页断言)
        L.i(' <========= test_enter_auto_page\n', tag=TAG)

    def test_play_large_screen(self):
        L.i('\n =========> test_play_large_screen, device: ' + self.deviceName, tag=TAG)
        self.operater.operate(PlayStartFullscreen.step_resize, self.deviceName)
        self.operater.operate(PlayStartFullscreen.step_start, self.deviceName)
        self.operater.operate(PlayStartFullscreen.step_CheckedTextView, self.deviceName)
        tools.sleep(5)
        self.operater.base_assert(PlayStartFullscreen.step_PLAYING断言)
        L.i(' <========= test_play_large_screen\n', tag=TAG)









    # def test_answer1(self, fixtrue_env):
    #     print('test_answer1.1: get fixtrue_env %s' % fixtrue_env)
    #     assert fixtrue_env == 10

    # def setup_module(module):
    #     print ("setup_module      module:%s" % module.__name__)
    #
    #
    # def teardown_module(module):
    #     print ("teardown_module   module:%s" % module.__name__)

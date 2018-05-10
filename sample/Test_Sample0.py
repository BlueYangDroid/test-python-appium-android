#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest
from testcase.TestBase import TestBase as testbase
from page.pages import *

TAG = 'TestSample0'

@pytest.mark.usefixtures("fixtrue_env")
class TestSample0(testbase):

    @pytest.mark.usefixtures("fixtrue_env")
    def test_something(self):
        print('=========> test_something click ------ device: ' + self.deviceName)

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
        self.operater.operate(PlayStartFullscreen.step_进入自动化测试页, self.deviceName)
        print('<========= test_something click ------ device: ' + self.deviceName)

#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import unittest
import selenium
import time
from appium import webdriver

from common.BaseOperate import OperateElement
from testcase.BaseCase import ParametrizedTestCase
from common.BaseElementEnmu import Action
from common.BaseElementEnmu import Option


class SampleCase(unittest.TestCase):

    def __init__(self, method_name='runTest', params=None):
        super(SampleCase, self).__init__(method_name)
        print('__init__ ------ ' + method_name)

    @classmethod
    def setUp(cls):
        # super().setUp()
        print('setUp ------ ')
        print('selenium version = ', selenium.__version__)
        cls.deviceName = '192.168.1.54:5555'
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '192.168.1.54:5555'
        desired_caps['appPackage'] = 'com.jamdeo.tv.vod'
        # desired_caps['app'] = 'F:\\build\outputs\apk\demo-L288-debug.apk'
        desired_caps['appActivity'] = 'com.hisense.base.MainActivity'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_Something(self):
        print('test_something click ------ ')
        self.operater = OperateElement(self.driver)

        time.sleep(2)
        # xpath：
        # self.driver.find_element_by_xpath(
        #     "//android.widget.ListView/android.widget.TextView[contains(@text, '自动化测试')]").click()
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
        self.operater.operate({
            Option.ELEMENT_INFO: '//android.widget.ListView/android.widget.TextView[contains(@text, "自动化测试")]',
            Option.FIND_TYPE: Action.FIND_ELEMENT_BY_XPATH,
            Option.ACTION: Action.CLICK,
            Option.CHECK_TIME: 5
        }, self.deviceName)


        # uiautomator - UiSelector：
        # name方式在1.5版本后已废除，能找到接口，不可使用，使用new UiSelector().text替代
        # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"海信广告测试\")").click()

        # class_name - child：
        # items = self.driver.find_elements_by_class_name('android.widget.TextView')
        # items[1].click()

        # id:
        # self.driver.find_element_by_id('com.hisense.vod:id/test_video_resize').click()
        self.play_large_screen()

    def play_large_screen(self):
        self.operater.operate({
            Option.ELEMENT_INFO: 'com.jamdeo.tv.vod:id/test_video_resize',
            Option.FIND_TYPE: Action.FIND_ELEMENT_BY_ID,
            Option.ACTION: Action.CLICK,
            Option.CHECK_TIME: 5
        }, self.deviceName)
        self.operater.operate({
            Option.ELEMENT_INFO: 'com.jamdeo.tv.vod:id/test_video_start',
            Option.FIND_TYPE: Action.FIND_ELEMENT_BY_ID,
            Option.ACTION: Action.CLICK,
            Option.CHECK_TIME: 5
        }, self.deviceName)
        self.operater.operate({
            Option.ELEMENT_INFO: 'android.widget.CheckedTextView',
            Option.FIND_TYPE: Action.FIND_ELEMENTS_BY_CLASS_NAME,
            Option.ACTION: Action.CLICK,
            Option.INDEX: 0,
            Option.CHECK_TIME: 5
        }, self.deviceName)
        time.sleep(10)
        self.operater.operate({
            Option.ELEMENT_INFO: 'com.jamdeo.tv.vod:id/test_video_status',
            Option.FIND_TYPE: Action.FIND_ELEMENT_BY_ID,
            Option.ACTION: Action.ASSERT,
            Option.ASSERT_VALUES: ('STATE_PLAYING', 'AD_STATE_PLAYING'),
            Option.CHECK_TIME: 5
        }, self.deviceName)

    @classmethod
    def tearDown(cls):
        print('tearDown ------ ')
        cls.driver.close_app()
        cls.driver.quit()
        pass

    @classmethod
    def setUpClass(cls):
        super(SampleCase, cls).setUpClass()
        print('setUpClass ------ ')

    @classmethod
    def tearDownClass(cls):
        super(SampleCase, cls).tearDownClass()
        print('tearDownClass ------ ')


if __name__ == '__main__':
    unittest.main()

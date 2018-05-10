#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re

import appium.common.exceptions
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
from common.BaseElementEnmu import Action
from common.BaseElementEnmu import Option
import time
import os
from utils.pylog import Log as L

'''
# 此脚本主要用于查找元素是否存在，操作页面元素
'''

TAG = 'BaseOperate'

def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class OperateElement:
    def __init__(self, driver: webdriver.Remote = ""):
        self.driver = driver

    def reset(self, driver: webdriver.Remote):
        """因为是单例,所以当driver变动的时候,需要重置一下driver

        Args:
            driver: driver

        """
        self.driver = driver
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']
        return self

    def findElement(self, operateInfo):
        '''
        查找元素.operateInfo,dict|list
        action：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            if type(operateInfo) == list:  # 多检查点
                if operateInfo.get("is_webview", "0") == 1:  # 1表示切换到webview
                    self.switchToWebview()
                elif operateInfo.get("is_webview", "0") == 2:
                    self.switchToNative()
                # if item.get("element_info", "0") == "0":  # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                #     return {"result": True}
                t = operateInfo[Option.CHECK_TIME] if operateInfo.get(Option.CHECK_TIME, "0") != "0" else Action.WAIT_TIME
                WebDriverWait(self.driver, t).until(lambda x: self.elements_by(operateInfo))
                return {"result": True}
            if type(operateInfo) == dict:  # 单检查点
                if operateInfo.get("is_webview", "0") == 1 and self.switchToWebview() is False:  # 1表示切换到webview
                    print("切换到webview失败，请确定是否在webview页面")
                    return {"result": False, "webview": False}
                elif operateInfo.get("is_webview", "0") == 2:
                    self.switchToNative()
                if operateInfo.get("element_info", "0") == "0":  # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                    return {"result": True}
                t = operateInfo["check_time"] if operateInfo.get("check_time",
                                                           "0") != "0" else Action.WAIT_TIME  # 如果自定义检测时间为空，就用默认的检测等待时间
                WebDriverWait(self.driver, t).until(lambda x: self.elements_by(operateInfo))  # 操作元素是否存在
                return {"result": True}
        except selenium.common.exceptions.TimeoutException:
            # print("查找元素" + mOperate["element_info"] + "超时")
            return {"result": False}
        except selenium.common.exceptions.NoSuchElementException:
            # print("查找元素" + mOperate["element_info"] + "不存在")
            return {"result": False}
        except selenium.common.exceptions.WebDriverException:
            print("WebDriver出现问题了")
            return {"result": False, "text": "selenium.common.exceptions.WebDriverException异常"}

    def operate(self, operateInfo, device):
        '''
        读取element的值,支持webview下获取值
        :param operateInfo:
            操作元素.operateInfo是字典
            element_info：元素详情, id/text/path...
            find_type: find类型
            index: elements 序号
            action：对应的操作
            test_info: 用例介绍
            device: 设备名
            code: 按键
            msg: set文本
        :param device:
        :return: result TRUE/FALSE
        '''
        L.i("---- operate ---- " + device, tag=TAG)
        res = self.findElement(operateInfo)
        if res["result"]:
            return self.operate_by(operateInfo, device)
        else:
            return res

    def operate_by(self, operateInfo, device):
        try:
            info = operateInfo.get(Option.ELEMENT_INFO, " ") + "_" + operateInfo.get(Option.ACTION, " ") + str(operateInfo.get(
                Option.CODE, " ")) + operateInfo.get(Option.MSG, " ")
            L.i("operate_by: " + info, tag=TAG)

            if operateInfo.get(Option.ACTION, "0") == "0":  # 如果没有此字段，说明没有相应操作，一般是检查点，直接判定为成功
                print("operate_by: just back true cause none action !")
                return {"result": True}
            actions = {
                Action.SWIPE_DOWN: lambda: self.swipeToDown(),
                Action.SWIPE_UP: lambda: self.swipeToUp(),
                Action.CLICK: lambda: self.click(operateInfo),
                Action.GET_VALUE: lambda: self.get_value(operateInfo),
                Action.SET_VALUE: lambda: self.set_value(operateInfo),
                Action.ADB_TAP: lambda: self.adb_tap(operateInfo, device),
                Action.GET_CONTENT_DESC: lambda: self.get_content_desc(operateInfo),
                Action.PRESS_KEY_CODE: lambda: self.press_keycode(operateInfo),
                Action.ASSERT: lambda: self.base_assert(operateInfo)
            }
            return actions[operateInfo.get(Option.ACTION)]()
        except IndexError:
            print(operateInfo["element_info"] + "索引错误")
            return {"result": False}

        except selenium.common.exceptions.NoSuchElementException:
            print(operateInfo["element_info"] + "页面元素不存在或没有加载完成")

            return {"result": False}
        except selenium.common.exceptions.StaleElementReferenceException:
            print(operateInfo["element_info"] + "页面元素已经变化")
            return {"result": False}
        except KeyError:
            # 如果key不存在，一般都是在自定义的page页面去处理了，这里直接返回为真
            return {"result": True}

    # 获取到元素到坐标点击，主要解决浮动层遮档无法触发driver.click的问题
    def adb_tap(self, operateInfo, device):
        print("adb_tap ----")

        bounds = self.elements_by(operateInfo).location
        x = str(bounds["x"])
        y = str(bounds["y"])

        cmd = "adb -s " + device + " shell input tap " + x + " " + y
        print(cmd)
        os.system(cmd)

        return {"result": True}

    def toast(self, xpath):
        print("toast ----")
        try:
            WebDriverWait(self.driver, 10, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
            return {"result": True}
        except selenium.common.exceptions.TimeoutException:
            return {"result": False}
        except selenium.common.exceptions.NoSuchElementException:
            return {"result": False}

    def check_find_single(self, find_type):
        if find_type in [Action.FIND_ELEMENT_BY_ID,
                          Action.FIND_ELEMENT_BY_XPATH,
                          Action.FIND_ELEMENT_BY_UISELECT_TEXT,
                          Action.FIND_ELEMENT_BY_CLASS_NAME]:
            return True
        elif find_type in [Action.FIND_ELEMENTS_BY_ID,
                            Action.FIND_ELEMENTS_BY_XPATH,
                            Action.FIND_ELEMENTS_BY_UISELECT_TEXT,
                            Action.FIND_ELEMENTS_BY_CLASS_NAME]:
            return False

    # 点击事件
    def click(self, operateInfo):
        print("click ----")
        find_type_ = operateInfo["find_type"]
        single = self.check_find_single(find_type_)

        if single:
            self.elements_by(operateInfo).click()
        else:
            self.elements_by(operateInfo)[operateInfo[Option.INDEX]].click()
        return {"result": True}

    # code 事件
    def press_keycode(self, operateInfo):
        print("press_keycode ----")
        self.driver.press_keycode(operateInfo.get("code", 0))
        return {"result": True}

    def get_content_desc(self, mOperate):
        result = self.elements_by(mOperate).get_attribute("contentDescription")
        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}

    '''
    切换native
    
    '''

    def switchToNative(self):
        print("switchToNative ----")
        self.driver.switch_to.context("NATIVE_APP")  # 切换到native

    '''
    切换webview
    '''

    def switchToWebview(self):
        print("switchToWebview ----")
        try:
            n = 1
            while n < 10:
                time.sleep(3)
                n = n + 1
                print(self.driver.contexts)
                for cons in self.driver.contexts:
                    if cons.lower().startswith("webview"):
                        self.driver.switch_to.context(cons)
                        # print(self.driver.page_source)
                        self.driver.execute_script('document.querySelectorAll("html")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("head")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("title")[0].style.display="block"')
                        print("切换webview成功")
                        return {"result": True}
            return {"result": False}
        except appium.common.exceptions.NoSuchContextException:
            print("切换webview失败")
            return {"result": False, "text": "appium.common.exceptions.NoSuchContextException异常"}

    # 左滑动
    def swipeLeft(self, operateInfo):
        print("swipeLeft ----")
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        x1 = int(width * 0.75)
        y1 = int(height * 0.5)
        x2 = int(width * 0.05)
        self.driver(x1, y1, x2, y1, 600)

    # swipe start_x: 200, start_y: 200, end_x: 200, end_y: 400, duration: 2000 从200滑动到400
    def swipeToDown(self):
        print("swipeToDown ----")
        height = self.driver.get_window_size()["height"]
        x1 = int(self.driver.get_window_size()["width"] * 0.5)
        y1 = int(height * 0.25)
        y2 = int(height * 0.75)

        self.driver.swipe(x1, y1, x1, y2, 1000)
        # self.driver.swipe(0, 1327, 500, 900, 1000)
        print("--swipeToDown--")
        return {"result": True}

    def swipeToUp(self):
        print("swipeToUp ----")
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4)
        print("执行上拉")
        return {"result": True}
        # for i in range(n):
        #     self.driver.swipe(540, 800, 540, 560, 0)
        #     time.sleep(2)

    def swipeToRight(self):
        print("swipeToRight ----")
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        x1 = int(width * 0.05)
        y1 = int(height * 0.5)
        x2 = int(width * 0.75)
        self.driver.swipe(x1, y1, x1, x2, 1000)
        # self.driver.swipe(0, 1327, 500, 900, 1000)
        print("--swipeToUp--")

    def set_value(self, operateInfo):
        """
        输入值，代替过时的send_keys
        :param operateInfo:
        :return:
        """
        print("set_value ----")
        find_type_ = operateInfo["find_type"]
        single = self.check_find_single(find_type_)

        if single:
            el = self.elements_by(operateInfo)
        else:
            el = self.elements_by(operateInfo)[operateInfo[Option.INDEX]]
        el.send_keys(operateInfo["msg"])

        try:
            self.driver.hide_keyboard()
        except:
            pass
        return {"result": True}

    def base_assert(self, operateInfo):
        """
        base_assert
        :param operateInfo:
        :return:
        """
        target = self.get_value(operateInfo)['text']
        print("base_assert ---- " + target)
        assert target in operateInfo.get(Option.ASSERT_VALUES)

    def get_value(self, operateInfo):
        '''
        读取element的值,支持webview下获取值
        :param operateInfo:
        :return:
        '''

        print("get_value ----")
        find_type_ = operateInfo["find_type"]
        single = self.check_find_single(find_type_)

        if single:
            el = self.elements_by(operateInfo)
        else:
            el = self.elements_by(operateInfo)[operateInfo[Option.INDEX]]

        if operateInfo.get("is_webview", "0") == 1:
            result = el.text
        else:
            result = el.get_attribute("text")

        re_reulst = re.findall(r'[\w+\u4e00-\u9fa5]', result)  # 匹配中文，大小写字母，数字，下划线, .
        return {"result": True, "text": "".join(re_reulst)}

    # 封装常用的标签
    def elements_by(self, operateInfo):
        info = operateInfo.get("element_info", " ") + ", find_type: " + operateInfo.get("find_type", " ")
        print("elements_by: " + info)
        element_info_ = operateInfo[Option.ELEMENT_INFO]
        find_type_ = operateInfo["find_type"]
        if find_type_ in [Action.FIND_ELEMENT_BY_UISELECT_TEXT, Action.FIND_ELEMENTS_BY_UISELECT_TEXT]:
            element_info_ = 'new UiSelector().text' + '(\"' + element_info_ + '\")'
        elements = {
            Action.FIND_ELEMENT_BY_ID: lambda: self.driver.find_element_by_id(element_info_),
            Action.FIND_ELEMENT_BY_XPATH: lambda: self.driver.find_element_by_xpath(element_info_),
            Action.FIND_ELEMENT_BY_UISELECT_TEXT: lambda: self.driver.find_element_by_android_uiautomator(element_info_),
            Action.FIND_ELEMENT_BY_CLASS_NAME: lambda: self.driver.find_element_by_class_name(element_info_),
            Action.FIND_ELEMENTS_BY_ID: lambda: self.driver.find_elements_by_id(element_info_),
            Action.FIND_ELEMENTS_BY_XPATH: lambda: self.driver.find_elements_by_xpath(element_info_),
            Action.FIND_ELEMENTS_BY_UISELECT_TEXT: lambda: self.driver.find_elements_by_android_uiautomator(element_info_),
            Action.FIND_ELEMENTS_BY_CLASS_NAME: lambda: self.driver.find_elements_by_class_name(element_info_)
        }
        return elements[operateInfo["find_type"]]()

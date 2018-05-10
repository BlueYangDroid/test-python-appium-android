#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest
import selenium
import time
from appium import webdriver

import sys
sys.path.append("..")

from common.BaseOperate import OperateElement
from common.Environment import Environment
from common.BaseElementEnmu import Action
from common.BaseElementEnmu import Option

from arch import activity as act
from arch import device as dev
from arch import hppium as ium


class TestBase:
    deviceName = ''
    operater = OperateElement()
    '''
    module/class/session/function(default).
    '''
    @pytest.fixture(scope="session")
    def fixtrue_env(self):
        print('--> base: setup fixtrue_env')


        hppium = ium.Hppium()
        hppium.start_driver()

        # self.operater = OperateElement(driver=hppium.get_driver()).reset(hppium.get_driver())
        # self.deviceName = hppium.get_device()
        TestBase.deviceName = hppium.get_device()
        TestBase.operater.reset(hppium.get_driver())
        print('---- operater prepared ----')

        yield
        print('<-- base: teardown fixtrue_env')
        hppium.stop_driver()




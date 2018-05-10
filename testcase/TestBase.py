#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest
import selenium
import time
from appium import webdriver

import sys
sys.path.append("..")

from common.BaseOperate import OperateElement
from arch import hppium as ium
from utils.pylog import Log as L

TAG = 'TestBase'


class TestBase:
    deviceName = ''
    operater = OperateElement()
    hppium = ium.Hppium()
    '''
    module/class/session/function(default).
    '''
    @pytest.fixture(scope="session")
    def fixtrue_env(self):
        L.i('------> base: setup fixtrue_env', tag=TAG)


        self.hppium.start_driver()

        # self.operater = OperateElement(driver=hppium.get_driver()).reset(hppium.get_driver())
        # self.deviceName = hppium.get_device()
        TestBase.deviceName = self.hppium.get_device()
        TestBase.operater.reset(self.hppium.get_driver())
        L.i('-------- base: operater prepared --------\n', tag=TAG)

        yield
        L.i('<------ base: teardown fixtrue_env', tag=TAG)
        self.hppium.stop_driver()




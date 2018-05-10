#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import os
import sys
from multiprocessing.pool import ThreadPool


sys.path.append("..")
from common.Environment import Environment
from common.AndroidDebugBridge import AndroidDebugBridge
from common.BaseAndroidPhone import get_phone_info
from lauch.AppiumServer import AppiumServer

import platform
from datetime import datetime
import testcase.PytestProxy as samplerunner

# foo: 当前目录下文件绝对路径
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def kill_adb():
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system(PATH("../app/kill5037.bat"))
    else:
        os.popen("killall adb")
    os.system("adb start-server")


def runnerPool(devices):
    devices_Pool = []

    for i in range(0, len(devices)):
        print("----- runnerPool ----- %s " % devices[i])
        _initdevice = {}
        _initdevice["deviceName"] = devices[i]["device"]
        # _initdevice["port"] = devices[i]["port"]
        _initdevice["platformVersion"] = get_phone_info(device=_initdevice["deviceName"])["release"]
        # _initdevice["platformVersion"] = "4.4.2"
        _initdevice["platformName"] = "android"
        _initdevice["appPackage"] = "com.jamdeo.tv.vod"
        _initdevice["appActivity"] = "com.hisense.base.MainActivity"
        # _initdevice["automationName"] = "uiautomator2"
        # _initdevice["systemPort"] = getDevices[i]["systemPort"]
        devices_Pool.append(_initdevice)

    # pool = ThreadPool(4) # 池的大小为4
    # pool.map(runner_device, devices_Pool)
    # close the pool and wait for the worker to exit
    # pool.close()
    # pool.join()
    runner_device(devices_Pool[0])


def runner_device(params):
    '''
    :param params: device + desired_caps
    :return:
    '''
    print("----runner_device------")
    starttime = datetime.now()
    # TestSuite 原生套件，bug！！！
    # suite = unittest.TestSuite()
    # # suite.addTests(ParametrizedTestCase.parametrize(SampleCase, params=params))
    # suite.addTest(unittest.makeSuite(SampleCase))
    # unittest.TextTestRunner().run(suite)     # verbosity=2 打印详细信息

    # pytest 扩展套件
    samplerunner.run()

    endtime = datetime.now()
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), " -> ", str((endtime - starttime).seconds) + "秒")


if __name__ == '__main__':

    # kill_adb()
    env = Environment()
    devicess = env.devices
    if len(devicess) > 0:

        l_devices = []
        for device in devicess:
            dev = {}
            dev["device"] = device

            # 多设备扩展初始化
            # init(dev)
            # dev["port"] = str(random.randint(4700, 4900))
            # dev["bport"] = str(random.randint(4700, 4900))
            # dev["systemPort"] = str(random.randint(4700, 4900))
            l_devices.append(dev)

        appium_server = AppiumServer(l_devices)
        appium_server.simple_start_server()

        runnerPool(l_devices)

        # writeExcel()  # 开始写报告
        appium_server.simple_stop_server()
    else:
        print("没有连接设备")

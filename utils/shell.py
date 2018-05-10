#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import platform

import subprocess

from arch import tools
from utils.pylog import Log as L

TAG = 'shell'

# 判断是否设置环境变量ANDROID_HOME
if "ANDROID_HOME" in os.environ:
    command = os.path.join(
        os.environ["ANDROID_HOME"],
        "platform-tools",
        "adb")

else:
    raise EnvironmentError(
        "Adb not found in $ANDROID_HOME path: %s." %
        os.environ["ANDROID_HOME"])


class Shell:
    @staticmethod
    def invoke(cmd):
        # shell设为true，程序将通过shell来执行
        # stdin, stdout, stderr分别表示程序的标准输入、输出、错误句柄。
        # 他们可以是PIPE，文件描述符或文件对象，也可以设置为None，表示从父进程继承。
        # subprocess.PIPE实际上为文本流提供一个缓存区
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o

    @staticmethod
    def get_android_devices():
        android_devices_list = Shell.get_devices_list()

        if len(android_devices_list) == 0:
            Shell.connect_config_device()
            tools.sleep(1)
            android_devices_list = Shell.get_devices_list()

        L.i('get_android_devices %s ' % str(android_devices_list), tag=TAG)
        return android_devices_list

    @staticmethod
    def connect_config_device():
        from common import config
        config = config.Config()
        device_name = config.get_config(config.TITLE_DEVICE, config.VALUE_DEVICE_NAME)
        L.i('connect_config_device %s ' % device_name, tag=TAG)
        ADB(device_name).connect()

    @staticmethod
    def get_devices_list():
        android_devices_list = []
        for device in Shell.invoke('adb devices').splitlines():
            if 'device' in device and 'devices' not in device:
                device = device.split('\t')[0]
                android_devices_list.append(device)
        return android_devices_list


class ADB(object):
    """
      参数:  device_id
    """

    def __init__(self, device_id=""):

        if device_id == "":
            self.device_id = ""
        else:
            self.connect_device_id = device_id
            self.device_id = "-s %s" % device_id

    def adb(self, args):
        cmd = "%s %s %s" % (command, self.device_id, str(args))
        return Shell.invoke(cmd)

    def connect(self):
        cmd = "%s connect %s" % (command, self.connect_device_id)
        return Shell.invoke(cmd)

    def shell(self, args):
        cmd = "%s %s shell %s" % (command, self.device_id, str(args),)
        return Shell.invoke(cmd)

    def get_device_state(self):
        """
        获取设备状态： offline | bootloader | device
        """
        return self.adb("get-state").stdout.read().strip()

    def get_device_id(self):
        """
        获取设备id号，return serialNo
        """
        return self.adb("get-serialno").stdout.read().strip()

    def get_android_version(self):
        """
        获取设备中的Android版本号，如4.2.2
        """
        return self.shell(
            "getprop ro.build.version.release").strip()

    def get_sdk_version(self):
        """
        获取设备SDK版本号
        """
        return self.shell("getprop ro.build.version.sdk").strip()

import selenium
from appium import webdriver

from arch import consts, device, activity
from arch import widget
from common.Environment import Environment


class Hppium(object):

    def __init__(self):
        super(Hppium, self).__init__()
        env = Environment().get_environment_info()
        split = env.devices[0].device_name.split(':')
        self._device = device.Device({
            "os_name": env.devices[0].platform_name,
            "os_version": env.devices[0].platform_version,
            "ip": split[0],
            "port": split[1]
        })
        self._activity = activity.Activity({
            "package": env.app_package,
            "class": env.app_activity
        })
        self._capabilities = {'platformName': env.devices[0].platform_name,
                        'platformVersion': env.devices[0].platform_version,
                        'deviceName': env.devices[0].device_name,
                        # 'app': env.apk,
                        # 'clearSystemFiles': True,
                        'appActivity': env.app_activity,
                        'appPackage': env.app_package,
                        # 'automationName': 'UIAutomator2',
                        # 'noSign': True
                        }



    def get_device_capabilities(self):
        # return {
        #     "platformName":     self._device._os_name,
        #     "platformVersion":  self._device._os_version,
        #     "deviceName":       self._device._name,
        #     "appPackage":       self._activity._package,
        #     "appActivity":      self._activity._class,
        # }
        return self._capabilities

    def get_driver(self):
        return self._driver

    def get_device(self):
        name_ = self._capabilities['deviceName']
        print('get_device %s = ' % name_)
        return name_

    def start_driver(self):
        print('selenium version = ', selenium.__version__)

        if not hasattr(self, '_driver'):
            print("driver is starting: " + self._device._name)
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", self.get_device_capabilities())
            print("driver is started: " + self._device._name)
        else:
            print("server is started: " + self._device._name)

    def stop_driver(self):
        if self._driver is None:
            print("server is stopped: " + self._device._name)
        else:
            print("driver is stopping: " + self._device._name)
            self._driver.close_app()
            self._driver.quit()
            self._driver = None
            print("driver is stopped: " + self._device._name)

    def send_key(self, key):
        if self._driver is None:
            print("you need call start_driver() first.")
        else:
            self._driver.press_keycode(key)

    def find_widget(self, params):
        if self._driver is None:
            print("you need call start_driver() first.")
            return None
        else:
            return widget.Widget(self._driver, params)


# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def init_driver(kws):
    # print('selenium version = ', selenium.__version__)
    # desired_caps = {}
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '4.4'
    # desired_caps['deviceName'] = '192.168.1.54:5555'
    # desired_caps['appPackage'] = 'com.hisense.vod'
    # # desired_caps['app'] = 'F:\\build\outputs\apk\demo-L288-debug.apk'
    # desired_caps['appActivity'] = 'com.hisense.base.MainActivity'
    # cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    desired_caps = {}

    desired_caps['appPackage'] = kws["appPackage"]
    desired_caps['appActivity'] = kws["appActivity"]
    desired_caps['udid'] = kws["deviceName"]

    desired_caps['platformVersion'] = kws["platformVersion"]
    desired_caps['platformName'] = kws["platformName"]
    desired_caps['deviceName'] = kws["deviceName"]
    # desired_caps["automationName"] = kws['automationName']
    # desired_caps["noReset"] = "True"
    # desired_caps['noSign'] = "True"
    # desired_caps["unicodeKeyboard"] = "True"
    # desired_caps["resetKeyboard"] = "True"
    # desired_caps["systemPort"] = kws["systemPort"]

    # desired_caps['app'] = devices["app"]

    print('Base init_driver ------ ')
    # remote = "http://127.0.0.1:" + str(kws["port"]) + "/wd/hub"
    remote = "http://127.0.0.1:" + "4723" + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    return driver


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should  
        inherit from this class.  
    """

    def __init__(self, methodName='runTest', params=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        print('Base __init__ ------ ' + methodName)


    @classmethod
    def setUpClass(cls):
        print('Base setUpClass ------ ')
        cls.driver = init_driver(gParams)
        cls.deviceName = gParams["deviceName"]


    def setUp(self):
        print('Base setUp ------ ')
        pass

    @classmethod
    def tearDownClass(cls):
        print('Base tearDownClass ------ ')
        cls.driver.close_app()
        cls.driver.quit()
        pass

    def tearDown(self):
        print('Base tearDown ------ ')
        pass

    @staticmethod
    def parametrize(case_class, params=None):
        print("Base parametrize ----- " + case_class.__name__)
        cases = []
        # print(param)
        testloader = unittest.TestLoader()
        # testnames = testloader.getTestCaseNames(case_class)
        # print("getTestCaseNames: " + "; ".join(testnames))

        # suite = unittest.TestSuite()
        # for name in testnames:
        #     suite.addTest(basecase_klass(name, params=params))
        # for name in testnames:
        #     print("Base append case: " + name)
        #     cases.append(case_class(name, params=params))

        # discover = unittest.defaultTestLoader.discover(casepath, pattern='test_*.py', top_level_dir=None)

        global gParams
        gParams = params
        cases = testloader.loadTestsFromModule(case_class)

        print("loadTestsFromModule: done")
        return cases

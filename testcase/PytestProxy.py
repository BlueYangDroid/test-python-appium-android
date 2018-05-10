#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest
import os
import sys

from page.PageGenerator import GenPages as gen

sys.path.append("..")
from utils.pylog import Log as log
from common.Environment import Environment
from utils.shell import Shell
from arch import device as dev

"""
run all case:
    python PytestProxy.py

run one module case:
    python PytestProxy.py test/test_home.py

run case with key word:
    python PytestProxy.py -k <keyword>

"""


def run():
    env = Environment()
    gen.gen_page_py()
    xml_report_path = env.get_environment_info().xml_report
    html_report_path = env.get_environment_info().html_report
    # 开始测试
    # extra_args = ['-s', '-q', '--alluredir', xml_report_path]
    extra_args = ['-s', '-q']
    # test_args = sys.argv[1:]
    test_args = [os.path.join(os.path.dirname(__file__), os.pardir, 'sample/Test_Sample2.py')
                 , os.path.join(os.path.dirname(__file__), os.pardir, 'sample/Test_Sample1.py')]
    pytest.main(extra_args + test_args)
    # # 生成html测试报告
    # cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)
    # try:
    #     Shell.invoke(cmd)
    # except:
    #     log.e("Html测试报告生成失败,确保已经安装了Allure-Commandline")


if __name__ == '__main__':
    run()
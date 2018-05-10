#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import yaml
import jinja2
import os
import os.path
import sys
sys.path.append("..")
from common.Environment import Environment
from common.config import Config
from utils.pylog import Log as L

pages_path = Environment().get_environment_info().pages_yaml
TAG = 'PageGenerator'

def parse():
    L.i('解析/page/yaml目录下所有yaml文件对象, Path:' + pages_path, tag=TAG)
    pages = {}
    for root, dirs, files in os.walk(pages_path):
        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'r', encoding='utf-8') as f:
                page = yaml.safe_load(f)
            pages.update(page)
        return pages


class GenPages:
    @staticmethod
    def gen_page_list():
        """
        将page.yaml文件对象转换成下面dict:
        return: {'HomePage': ['登录入口'], 'LoginPage': ['账户', '密码', '登录']}
        从yaml过滤出page: step_names[]
        """
        _page_list = {}
        pages = parse()
        for page, value in pages.items():
            steps = value['steps']
            step_names = []
            for step in steps:
                step_names.append(step['name'])
            _page_list[page] = step_names
        return _page_list

    @staticmethod
    def gen_page_py():
        """
        利用jinja2生成pages.py文件，在模板中组织成page: steps
        """
        base_dir = Config.BASE_PATH_DIR
        template_loader = jinja2.FileSystemLoader(searchpath=base_dir + "/page/template")
        template_env = jinja2.Environment(loader=template_loader)
        page_list = GenPages.gen_page_list()
        print(page_list)

        # 模板pages中定义的model为'page_list', 此字段不能动
        _templateVars = {
            'page_list': page_list
        }
        template = template_env.get_template("pages")
        path_pages_py_ = base_dir + '/page/pages.py'
        if os.path.isfile(path_pages_py_):
            os.remove(path_pages_py_)
        with open(path_pages_py_, 'w', encoding='utf-8') as f:
            f.write(template.render(_templateVars))


if __name__ == '__main__':
    GenPages.gen_page_py()

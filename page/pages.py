#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from page import PageGenerator as gen

pages = gen.parse()


def get_step(page_name, step_name):
    '''
    根据事先yaml加载过滤后的page-step_names数据, 还原各个step的详情字典数据
    :param page_name:
    :param step_name:
    :return:
    '''
    steps = pages[page_name]['steps']
    for step in steps:
        if step['name'] == step_name:
            return step


class HomePageToSign:
    
    step_登录按钮 = get_step('HomePageToSign', '登录按钮')
    


class LoginPage:
    
    step_账户 = get_step('LoginPage', '账户')
    
    step_密码 = get_step('LoginPage', '密码')
    
    step_登录 = get_step('LoginPage', '登录')
    


class HomePageSigned:
    
    step_登录断言 = get_step('HomePageSigned', '登录断言')
    


class PlayStartFullscreen:
    
    step_进入自动化测试页 = get_step('PlayStartFullscreen', '进入自动化测试页')
    
    step_resize = get_step('PlayStartFullscreen', 'resize')
    
    step_start = get_step('PlayStartFullscreen', 'start')
    
    step_CheckedTextView = get_step('PlayStartFullscreen', 'CheckedTextView')
    
    step_PLAYING断言 = get_step('PlayStartFullscreen', 'PLAYING断言')
    






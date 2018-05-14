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
    
    step_启动首页 = get_step('PlayStartFullscreen', '启动首页')
    
    step_进入自动化测试页 = get_step('PlayStartFullscreen', '进入自动化测试页')
    
    step_测试页断言 = get_step('PlayStartFullscreen', '测试页断言')
    
    step_resize = get_step('PlayStartFullscreen', 'resize')
    


class PlayCaseQiyi:
    
    step_右划侧栏 = get_step('PlayCaseQiyi', '右划侧栏')
    
    step_奇艺菜单 = get_step('PlayCaseQiyi', '奇艺菜单')
    
    step_start = get_step('PlayCaseQiyi', 'start')
    
    step_CheckedTextView = get_step('PlayCaseQiyi', 'CheckedTextView')
    
    step_PLAYING断言 = get_step('PlayCaseQiyi', 'PLAYING断言')
    


class PlayCaseWasu:
    
    step_右划侧栏 = get_step('PlayCaseWasu', '右划侧栏')
    
    step_华数菜单 = get_step('PlayCaseWasu', '华数菜单')
    
    step_start = get_step('PlayCaseWasu', 'start')
    
    step_CheckedTextView = get_step('PlayCaseWasu', 'CheckedTextView')
    
    step_PLAYING断言 = get_step('PlayCaseWasu', 'PLAYING断言')
    


class PlayCaseTencent:
    
    step_右划侧栏 = get_step('PlayCaseTencent', '右划侧栏')
    
    step_腾讯菜单 = get_step('PlayCaseTencent', '腾讯菜单')
    
    step_start = get_step('PlayCaseTencent', 'start')
    
    step_CheckedTextView = get_step('PlayCaseTencent', 'CheckedTextView')
    
    step_PLAYING断言 = get_step('PlayCaseTencent', 'PLAYING断言')
    


class PlayCaseSohu:
    
    step_右划侧栏 = get_step('PlayCaseSohu', '右划侧栏')
    
    step_搜狐菜单 = get_step('PlayCaseSohu', '搜狐菜单')
    
    step_start = get_step('PlayCaseSohu', 'start')
    
    step_CheckedTextView = get_step('PlayCaseSohu', 'CheckedTextView')
    
    step_PLAYING断言 = get_step('PlayCaseSohu', 'PLAYING断言')
    


class PlayCaseWangsu:
    
    step_右划侧栏 = get_step('PlayCaseWangsu', '右划侧栏')
    
    step_网宿菜单 = get_step('PlayCaseWangsu', '网宿菜单')
    
    step_start = get_step('PlayCaseWangsu', 'start')
    
    step_CheckedTextView = get_step('PlayCaseWangsu', 'CheckedTextView')
    
    step_PLAYING断言 = get_step('PlayCaseWangsu', 'PLAYING断言')
    


class PlayCaseUrl:
    
    step_右划侧栏 = get_step('PlayCaseUrl', '右划侧栏')
    
    step_URL菜单 = get_step('PlayCaseUrl', 'URL菜单')
    
    step_start = get_step('PlayCaseUrl', 'start')
    
    step_CheckedTextView = get_step('PlayCaseUrl', 'CheckedTextView')
    
    step_PLAYING断言 = get_step('PlayCaseUrl', 'PLAYING断言')
    






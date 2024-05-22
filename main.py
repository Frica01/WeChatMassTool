# -*- coding: utf-8 -*-
# Name:         main.py
# Author:       小菜
# Date:         2024/4/01 00:00
# Description:


import datetime
import platform
import sys
from ctypes import windll

import PySide6
import uiautomation
from PySide6 import QtGui
from PySide6.QtWidgets import (QApplication, QMessageBox, QWidget)
from cprint import cprint
from tendo import singleton

from config import (Animate, WeChat)
from controllers import ControllerMain
from utils import (get_specific_process, get_resource_path, get_config, minimize_wechat)
from version import (__version__, __project_name__, __author__)


def set_app_user_model_id():
    """设置应用程序用户模型ID"""
    try:
        myapp_id = 'myapp_id'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
    except ImportError:
        pass


def print_startup_info():

    # 获取系统信息
    system_info = platform.uname()

    Bot_Logo = r""" 
    
    /¯¯¯¯\         /¯¯¯¯\         /¯¯¯¯\     
  o-|[][]|-o     o-|[][]|-o     o-|[][]|-o   
    |_--_|         |_--_|         |_--_|     
 /¯¯¯¯¯¯¯¯¯¯\   /¯¯¯¯¯¯¯¯¯¯\   /¯¯¯¯¯¯¯¯¯¯\  
 |||  «»  |||   |||  «»  |||   |||  «»  |||  
 |||      |||   |||      |||   |||      |||  
(o)|      |(o) (o)|      |(o) (o)|      |(o) 
   |  ||  |       |  ||  |       |  ||  |    
   |__||__|       |__||__|       |__||__|    
   |__||__|       |__||__|       |__||__|
"""
    # 启动信息
    startup_info = f"""
        项目名称: {__project_name__}
        版本: {__version__}
        作者: {__author__}
        启动时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        系统: {system_info.system} {system_info.release}
        版本: {system_info.version}
        处理器: {system_info.processor}
        Python: {platform.python_version()}
        PySide6: {PySide6.__version__}
        uiautomation: {uiautomation.version.VERSION}

        项目启动中...
    """
    cprint.info(Bot_Logo.rstrip('\n'))
    cprint.info(startup_info.rstrip('\n'))


def check_wechat_running():
    """检查微信是否运行"""
    if not get_specific_process(proc_name=WeChat.PROCESS_NAME):
        QMessageBox.critical(QWidget(), '报错咯', "微信未启动!")
        sys.exit()  # 退出程序


def initialize_application():
    app = QApplication()
    app.setWindowIcon(QtGui.QIcon(get_resource_path(r'views/resources/images/favicon.ico')))
    check_wechat_running()
    # 获取默认配置, 看是否需要以动画形式启动
    controller = ControllerMain(get_config(WeChat.APP_NAME, section=Animate.SECTION, option=Animate.OPTION))
    # 绑定退出事件, 关闭微信窗口
    app.aboutToQuit.connect(lambda: minimize_wechat(WeChat.WINDOW_CLASSNAME, name=WeChat.WINDOW_NAME))
    sys.exit(app.exec())


def main():
    """主入口"""
    try:
        singleton.SingleInstance()  # 将检查是否已有实例运行
    except singleton.SingleInstanceException:
        sys.exit()  # 如果已有实例运行，退出程序
    # 正常启动流程
    set_app_user_model_id()
    print_startup_info()  # 打印启动信息
    initialize_application()


if __name__ == '__main__':
    main()

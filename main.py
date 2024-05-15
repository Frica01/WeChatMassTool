# -*- coding: utf-8 -*-
# Name:         main.py
# Author:       小菜
# Date:         2024/4/01 00:00
# Description:


import sys
from ctypes import windll

from PySide6 import QtGui
from PySide6.QtWidgets import (QApplication, QMessageBox, QWidget)

from config import (Animate, WeChat)
from controllers import ControllerMain
from utils import (get_specific_process, get_resource_path, get_config, minimize_wechat)

# 这段代码放在前面即可
try:
    myapp_id = 'myapp_id'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
except ImportError:
    pass


if __name__ == '__main__':

    app = QApplication()
    app.setWindowIcon(QtGui.QIcon(get_resource_path(r'views/resources/images/favicon.ico')))
    if get_specific_process(proc_name=WeChat.PROCESS_NAME):
        # 获取默认配置, 看是否需要以动画形式启动
        controller = ControllerMain(get_config(WeChat.APP_NAME, section=Animate.SECTION, option=Animate.OPTION))
        # 绑定退出事件, 关闭微信窗口
        app.aboutToQuit.connect(lambda: minimize_wechat(WeChat.WINDOW_CLASSNAME, name=WeChat.WINDOW_NAME))
        sys.exit(app.exec())
    else:
        QMessageBox.critical(QWidget(), '报错咯', "微信未启动!")
        sys.exit()  # 退出程序

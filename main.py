# -*- coding: utf-8 -*-
# Name:         main.py
# Author:       小菜
# Date:         2024/4/01 00:00
# Description:
import os
import sys

from PySide6 import QtGui
from PySide6.QtWidgets import (QApplication, QMessageBox, QWidget)

from config import PROCESS_NAME
from controllers import ControllerMain
from utils import (get_specific_process, get_resource_path)

from ctypes import windll

# 这段代码放在前面即可
try:
    myapp_id = 'myapp_id'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
except ImportError:
    pass


if __name__ == '__main__':
    app = QApplication()
    app.setWindowIcon(QtGui.QIcon(get_resource_path(r'views/resources/images/微信-4.png')))
    if get_specific_process(proc_name=PROCESS_NAME):
        controller = ControllerMain(animate_on_startup=True)
        sys.exit(app.exec())
    else:
        QMessageBox.critical(QWidget(), '报错咯', "微信未启动!")
        sys.exit()  # 退出程序



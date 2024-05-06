# -*- coding: utf-8 -*-
# Name:         view_main.py
# Author:       小菜
# Date:         2024/4/01 00:00
# Description:


from PySide6.QtCore import Qt

from views import (MainWindow, LoginWindow)
from views.ui_components import (create_animation_group, create_opacity_animation)


class ViewMain(MainWindow):
    login_window: LoginWindow

    def __init__(self, animate_on_startup):
        super().__init__()

        # 判断是否以动画的形式启动
        if animate_on_startup:
            self.login_window = LoginWindow()
            # 设置窗口不显示任务栏
            self.login_window.setWindowFlag(Qt.Tool)
            # 连接Signal信号，login动画加载完成再运行
            self.login_window.login_successful.connect(self.start_animation)
            #
            self.login_window.show()
        else:
            self.show()
            # 主窗口淡入，看个人喜好
            # self.fade_in = create_opacity_animation(self.main_window, 0, 1, 2500)
            # self.fade_in.start()

    def start_animation(self):
        # 确保第二个窗口的透明度初始为0
        self.setWindowOpacity(0)
        self.show()

        # 创建淡出淡入动画
        fade_out = create_opacity_animation(self.login_window, 1, 0, 1800)
        fade_in = create_opacity_animation(self, 0, 1, 2500)
        fade_out.finished.connect(self.login_window.close)  # 淡出完成后隐藏窗口

        # 使用并行动画组合，同时执行淡入和淡出
        self.animation_group = create_animation_group((fade_out, fade_in))
        self.animation_group.start()

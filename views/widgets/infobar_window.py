# -*- coding: utf-8 -*-
# Name:         infobar_window.py
# Author:       小菜
# Date:         2024/5/23 上午01:09
# Description:

from PySide6.QtCore import (Qt, QTimer, QPropertyAnimation, QPoint)
from PySide6.QtWidgets import (QFrame, QGraphicsOpacityEffect)

from views.ui_components import create_opacity_animation
from views.ui_designs import Ui_InfoBar


class InfoBarWindow(QFrame, Ui_InfoBar):
    animation: QPropertyAnimation
    opacity_animation: QPropertyAnimation

    def __init__(self, parent=None, message: str = str(), icon_type='success'):
        super(InfoBarWindow, self).__init__(parent)
        self.setupUi(self)
        # 独立窗口
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # 透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置提示文本
        self.prompt_info_label.setText(str(message))
        self.prompt_icon_label.setStyleSheet(f"image: url(:/icons/icons/status-{icon_type}.png);")
        self.btn_close_prompt.clicked.connect(self.close_animation)
        self.show()

        # 计时器在4秒后关闭 InfoBar
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_animation)
        self.timer.start(4000)

    def show_animation(self):
        """动画从下到上淡入 InfoBar。"""
        start_pos = self.calculate_start_pos()
        end_pos = self.calculate_end_pos()
        self.animation = create_opacity_animation(self, start_pos, end_pos, 800, property_name=b'pos')
        self.animation.start()

    def close_animation(self):
        """动画淡出 InfoBar 然后从父窗口中移除。"""
        opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacity_effect)
        self.opacity_animation = create_opacity_animation(opacity_effect, 1, 0, 500, b'opacity')
        self.opacity_animation.finished.connect(self._remove_from_parent)
        self.opacity_animation.start()

    def _remove_from_parent(self):
        """将 InfoBar 从父窗口的列表中移除并关闭。"""
        if self in self.parent().infobars:
            self.parent().infobars.remove(self)
            self.parent().update_infobars_position()  # 移除后更新位置
        self.close()

    def calculate_start_pos(self):
        """计算窗口移动的起始点坐标"""
        parent_geometry = self.parent().geometry()
        # 相对于父窗口右边缘的50像素间隔, 从父窗口底部开始
        return QPoint(
            parent_geometry.right() - self.width() - 50,
            (parent_geometry.top() + parent_geometry.height()) * 0.66
        )

    def calculate_end_pos(self):
        """计算 InfoBar 的目标位置"""
        parent_geometry = self.parent().geometry()
        index = self.parent().infobars.index(self)
        return QPoint(
            parent_geometry.right() - self.width() - 50,
            parent_geometry.top() + 40 + (self.height() + 10) * index
        )

# -*- coding: utf-8 -*-
# Name:         ui_setup.py
# Author:       小菜
# Date:         2024/4/01 00:00
# Description:  一些ui公共方法

from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QGraphicsDropShadowEffect, QWidget)


def apply_shadow_effect(self, blur_radius=10, x_offset=0, y_offset=0, color=(0, 0, 0, 150)):
    """为指定的小部件应用阴影效果。

    Args:
        self(QWidget): 要应用阴影效果的小部件.
        blur_radius(int): 阴影的模糊半径.
        x_offset(int): 阴影的X轴偏移量.
        y_offset(int): 阴影的Y轴偏移量.
        color: 表示阴影RGBA颜色的元组.
    """
    self.shadow = QGraphicsDropShadowEffect(self)
    self.shadow.setBlurRadius(blur_radius)
    self.shadow.setXOffset(x_offset)
    self.shadow.setYOffset(y_offset)
    self.shadow.setColor(QColor(*color))
    self.setGraphicsEffect(self.shadow)

# -*- coding: utf-8 -*-
# Name:         animations.py
# Author:       小菜
# Date:         2024/4/01 00:00
# Description:

from typing import (Iterable, Union)

from PySide6.QtCore import (QEasingCurve, QPropertyAnimation, QParallelAnimationGroup)
from PySide6.QtWidgets import QWidget, QGraphicsOpacityEffect


def create_width_animation(widget: QWidget, target_width: int, duration=800):
    """在指定的持续时间内，将侧边面板控件的宽度动画化到目标宽度。

    Args:
        widget(QWidget): 要动画化的QWidget对象。
        target_width(int): 动画化到的目标宽度，以像素为单位。
        duration(int): 动画持续时间，以毫秒为单位，默认值800

    Returns:
        返回配置好的动画对象(QPropertyAnimation)

    """
    animation = QPropertyAnimation(widget, b"minimumWidth")
    animation.setDuration(duration)
    animation.setStartValue(widget.width())
    animation.setEndValue(target_width)
    animation.setEasingCurve(QEasingCurve.InOutQuart)
    return animation


def create_opacity_animation(widget: Union[QWidget, QGraphicsOpacityEffect], target_start, target_end, duration=1800,
                             property_name=b'windowOpacity'):
    """在指定的持续时间内，将侧边面板控件的宽度动画化到目标宽度。

    Args:

        widget (Union[QWidget, QGraphicsOpacityEffect]): 要动画化的对象，可以是QWidget或QGraphicsOpacityEffect。
        target_start(int): 动画的起始透明度值。0 表示完全透明，1 表示完全不透明。
        target_end(int): 动画的结束透明度值。取值范围同上。
        duration(int): 动画持续时间，以毫秒为单位，默认值1800
        property_name(bytes): 要动画化的属性名称，默认值为b"windowOpacity"。

    Returns:
        返回配置好的动画对象(QPropertyAnimation)

    """
    animation = QPropertyAnimation(widget, property_name)
    animation.setDuration(duration)
    animation.setStartValue(target_start)
    animation.setEndValue(target_end)
    animation.setEasingCurve(QEasingCurve.InOutQuad)
    return animation


def create_animation_group(animations: Iterable):
    """ 创建动画组
    Args:
        animations(Iterable): 动画组成员

    Returns:
        动画组对象(QParallelAnimationGroup)

    """
    animation_group = QParallelAnimationGroup()
    for anim in animations:
        animation_group.addAnimation(anim)
    return animation_group

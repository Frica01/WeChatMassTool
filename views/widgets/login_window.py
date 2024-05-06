# -*- coding: utf-8 -*-
# Name:         login_window.py
# Author:       小菜
# Date:         2024/4/01 00:00
# Description:

import sys

from PySide6.QtCore import (Qt, QTimer, QPropertyAnimation, QRect, QEasingCurve, Signal)
from PySide6.QtGui import (QColor, QPainter, QFont, QPen, QIcon)
from PySide6.QtWidgets import (QMainWindow, QGraphicsDropShadowEffect, QWidget, QApplication)

from views.ui_components import apply_shadow_effect
from views.ui_designs import Ui_Login


class LoginWindow(QMainWindow):
    animation: QPropertyAnimation
    login_successful = Signal()

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setAttribute(Qt.WA_TranslucentBackground)

        # IMPORT CIRCULAR PROGRESS
        self.progress = CircularProgress()
        self.progress.width = 240
        self.progress.height = 240
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow()
        self.progress.progress_width = 4
        self.progress.progress_color = QColor("#bdff00")
        self.progress.text_color = QColor("#E6E6E6")
        self.progress.bg_color = QColor("#222222")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()

        # ADD DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.bg.setGraphicsEffect(self.shadow)

        # QTIMER
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        # KEY PRESS EVENT
        # self.show()
        #
        self.counter = int()

    def shake_window(self):
        # SHAKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))

    # UPDATE PROGRESS BAR
    def update(self):
        # global counter

        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(self.counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if self.counter >= 100:
            # STOP TIMER
            self.timer.stop()
            self.animation_login()
        # INCREASE COUNTER
        self.counter += 1

    # START ANIMATION TO LOGIN
    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -380, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        # 登录成功，发射信号
        self.animation.finished.connect(lambda: QTimer.singleShot(800, self.login_successful.emit))


class CircularProgress(QWidget):
    shadow: QGraphicsDropShadowEffect

    def __init__(self):
        QWidget.__init__(self)

        # CUSTOM PROPERTIES
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.max_value = 100
        self.progress_color = 0xff79c6
        # Text
        self.enable_text = True
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0xff79c6
        # BG
        self.enable_bg = True
        self.bg_color = 0x44475a

        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)

    # ADD DROP_SHADOW
    def add_shadow(self):
        apply_shadow_effect(self, 15, 0, 0, (0, 0, 0, 80))

    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint()  # Render progress bar after change value

    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, e):
        # SET PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)  # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # PEN
        pen = QPen()
        pen.setWidth(self.progress_width)
        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # ENABLE BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, 0, 360 * 16)

        # CREATE ARC / CIRCULAR PROGRESS
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)

        # CREATE TEXT
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # END
        paint.end()


if __name__ == "__main__":
    # APPLICATION
    app = QApplication()
    app.setWindowIcon(QIcon("icon.ico"))
    window = LoginWindow()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QProgressBar, QPushButton, QRadioButton, QSizePolicy, QStackedWidget, QTextEdit,
                               QVBoxLayout, QWidget)
from .resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(
            u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "\n"
            "SET APP STYLESHEET - FULL STYLES HERE\n"
            "DARK THEME - DRACULA COLOR BASED\n"
            "\n"
            "///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
            "\n"
            "QWidget{\n"
            "	color: rgb(221, 221, 221);\n"
            "	font: 10pt \"Microsoft YaHei UI\";\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Tooltip */\n"
            "QToolTip {\n"
            "	color: #ffffff;\n"
            "	background-color: rgba(33, 37, 43, 180);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "	background-image: none;\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 2px solid rgb(255, 121, 198);\n"
            "	text-align: left;\n"
            "	padding-left: 8px;\n"
            "	margin: 0px;\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Bg App */\n"
            "#bgApp {	\n"
            "	"
            "background-color: rgb(40, 44, 52);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Left Menu */\n"
            "#leftMenuBg {	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#topLogo {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	background-image: url(:/images/images/WeChatMass.png);\n"
            "	background-position: centered;\n"
            "	background-repeat: no-repeat;\n"
            "}\n"
            "#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
            "#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
            "\n"
            "/* MENUS */\n"
            "#topMenu .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color: transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#topMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#topMenu .QPushButton:pressed {	\n"
            "	background-color: rg"
            "b(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "#bottomMenu .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 20px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#bottomMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#bottomMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "#leftMenuFrame{\n"
            "	border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Toggle Button */\n"
            "#toggleButton {\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 20px solid transparent;\n"
            "	background-color: rgb(37, 41, 48);\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "	color: rgb(113, 126, 149);\n"
            "}\n"
            "#toggleButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#toggleButton:pressed {\n"
            "	background-color: "
            "rgb(189, 147, 249);\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "#titleRightInfo { padding-left: 10px; }\n"
            "\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Extra Tab */\n"
            "#extraLeftBox {	\n"
            "	background-color: rgb(44, 49, 58);\n"
            "}\n"
            "#extraTopBg{	\n"
            "	background-color: rgb(189, 147, 249)\n"
            "}\n"
            "\n"
            "/* Icon */\n"
            "#extraIcon {\n"
            "	background-position: center;\n"
            "	background-repeat: no-repeat;\n"
            "	background-image: url(:/icons/icons/icon_settings.png);\n"
            "}\n"
            "\n"
            "/* Label */\n"
            "#extraLabel { color: rgb(255, 255, 255); }\n"
            "\n"
            "/* Btn Close */\n"
            "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
            "#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* Extra Content */\n"
            "#extraContent{\n"
            "	border-to"
            "p: 3px solid rgb(40, 44, 52);\n"
            "}\n"
            "\n"
            "/* Extra Top Menus */\n"
            "#extraTopMenu .QPushButton {\n"
            "background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	/*border-left: 22px solid transparent;*/\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	/*padding-left: 44px;*/\n"
            "}\n"
            "#extraTopMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#extraTopMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Content App */\n"
            "#contentTopBg{	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#contentBottom{\n"
            "	border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Top Buttons */\n"
            "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); borde"
            "r-style: solid; border-radius: 4px; }\n"
            "#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* Theme Settings */\n"
            "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
            "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
            "\n"
            "/* Bottom Bar */\n"
            "#bottomBar { background-color: rgb(44, 49, 58); }\n"
            "#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "/* CONTENT SETTINGS */\n"
            "/* MENUS */\n"
            "#contentSettings .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#contentSettings .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#contentSettings .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color"
            ": rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "LineEdit */\n"
            "QLineEdit {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding-left: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "QTextEdit */\n"
            "QTextEdit {\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	padding: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            " }\n"
            "QTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            " }\n"
            "QTextEdit:hover {\n"
            ""
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QTextEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ScrollBars */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "	border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-width: 25px;\n"
            "	border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-right-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    subcontrol-"
            "position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(189, 147, 249);\n"
            "    min-height: 25px;\n"
            "	border-radius: 4px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-bottom-left-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "	border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-top-right-"
            "radius: 4px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "CheckBox */\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "	background-image: url(:/icons/icons/cil-check-alt.png);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "RadioButton */\n"
            "QRadioButton::in"
            "dicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QRadioButton::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "    background: 3px solid rgb(94, 106, 130);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ComboBox */\n"
            "QComboBox{\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "	subcontrol-origin: padding;\n"
            "	subcontrol-position: top right;\n"
            "	width: 25px; \n"
            "	border-left-width: 3px;\n"
            "	border-left-color: rgba(39, 44, 54, 150);\n"
            "	border-left-style: solid;\n"
            "	border-top-right-radius: 3px;\n"
            "	border-bottom-right-r"
            "adius: 3px;	\n"
            "	background-image: url(:/icons/icons/cil-arrow-bottom.png);\n"
            "	background-position: center;\n"
            "	background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "	color: rgb(255, 121, 198);	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	padding: 10px;\n"
            "	selection-background-color: rgb(39, 44, 54);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Sliders */\n"
            "QSlider::groove:horizontal {\n"
            "    border-radius: 5px;\n"
            "    height: 10px;\n"
            "	margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:horizontal:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:horizontal {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "    border: none;\n"
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:horizontal:pressed {\n"
            ""
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "QSlider::groove:vertical {\n"
            "    border-radius: 5px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:vertical:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:vertical {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "	border: none;\n"
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:vertical:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:vertical:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Button */\n"
            "#pagesContainer QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "#pagesContainer QPushButton:hover {\n"
            "	background-color: rgb(57, 65, 80);\n"
            "	border: 2px soli"
            "d rgb(61, 70, 86);\n"
            "}\n"
            "#pagesContainer QPushButton:pressed {	\n"
            "	background-color: rgb(35, 40, 49);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}\n"
            "")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        self.titleLeftApp.setStyleSheet(u"")
        self.titleLeftApp.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftDescription.setFont(font1)
        self.titleLeftDescription.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.toggleButton.setFont(font2)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_page_home = QPushButton(self.topMenu)
        self.btn_page_home.setObjectName(u"btn_page_home")
        sizePolicy.setHeightForWidth(self.btn_page_home.sizePolicy().hasHeightForWidth())
        self.btn_page_home.setSizePolicy(sizePolicy)
        self.btn_page_home.setMinimumSize(QSize(0, 45))
        self.btn_page_home.setFont(font2)
        self.btn_page_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_page_home.setStyleSheet(u"background-image: url(:/icons/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_page_home)

        self.btn_page_pending = QPushButton(self.topMenu)
        self.btn_page_pending.setObjectName(u"btn_page_pending")
        self.btn_page_pending.setMinimumSize(QSize(0, 45))
        self.btn_page_pending.setFont(font2)
        self.btn_page_pending.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_pending.setStyleSheet(u"background-image: url(:/icons/icons/friend.png);")

        self.verticalLayout_8.addWidget(self.btn_page_pending)

        self.btn_page_msg = QPushButton(self.topMenu)
        self.btn_page_msg.setObjectName(u"btn_page_msg")
        sizePolicy.setHeightForWidth(self.btn_page_msg.sizePolicy().hasHeightForWidth())
        self.btn_page_msg.setSizePolicy(sizePolicy)
        self.btn_page_msg.setMinimumSize(QSize(0, 45))
        self.btn_page_msg.setFont(font2)
        self.btn_page_msg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_msg.setLayoutDirection(Qt.LeftToRight)
        self.btn_page_msg.setStyleSheet(u"background-image: url(:/icons/icons/cli-msg.png);")

        self.verticalLayout_8.addWidget(self.btn_page_msg)

        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleTheme = QPushButton(self.bottomMenu)
        self.toggleTheme.setObjectName(u"toggleTheme")
        sizePolicy.setHeightForWidth(self.toggleTheme.sizePolicy().hasHeightForWidth())
        self.toggleTheme.setSizePolicy(sizePolicy)
        self.toggleTheme.setMinimumSize(QSize(0, 45))
        self.toggleTheme.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleTheme.setStyleSheet(u"background-image: url(:/icons/icons/cli-switch-theme-1.png);")
        self.toggleTheme.setCheckable(False)

        self.verticalLayout_9.addWidget(self.toggleTheme)

        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font2)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)

        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

        self.verticalLayout_5.addLayout(self.extraTopLayout)

        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setStyleSheet(u"font: 450 11pt\"Segoe UI\";\n"
                                        "")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 6, -1, 6)
        self.frame_9 = QFrame(self.extraTopMenu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_17.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.cb_text_interval = QComboBox(self.frame_9)
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.addItem("")
        self.cb_text_interval.setObjectName(u"cb_text_interval")
        self.cb_text_interval.setMinimumSize(QSize(120, 0))
        self.cb_text_interval.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.cb_text_interval, 0, Qt.AlignRight)

        self.verticalLayout_11.addWidget(self.frame_9, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.extraTopMenu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.cb_file_interval = QComboBox(self.frame_4)
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.addItem("")
        self.cb_file_interval.setObjectName(u"cb_file_interval")
        self.cb_file_interval.setMinimumSize(QSize(120, 0))
        self.cb_file_interval.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.cb_file_interval, 0, Qt.AlignRight)

        self.verticalLayout_11.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_15 = QFrame(self.extraTopMenu)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 40))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.radio_btn_animate_true = QRadioButton(self.frame_15)
        self.radio_btn_animate_true.setObjectName(u"radio_btn_animate_true")
        self.radio_btn_animate_true.setCursor(QCursor(Qt.PointingHandCursor))
        self.radio_btn_animate_true.setChecked(True)

        self.horizontalLayout_11.addWidget(self.radio_btn_animate_true)

        self.radio_btn_animate_false = QRadioButton(self.frame_15)
        self.radio_btn_animate_false.setObjectName(u"radio_btn_animate_false")
        self.radio_btn_animate_false.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.radio_btn_animate_false)

        self.verticalLayout_11.addWidget(self.frame_15, 0, Qt.AlignLeft)

        self.frame_17 = QFrame(self.extraTopMenu)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 40))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setSpacing(20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_19.addWidget(self.label_7)

        self.radio_btn_enter = QRadioButton(self.frame_17)
        self.radio_btn_enter.setObjectName(u"radio_btn_enter")
        self.radio_btn_enter.setChecked(True)

        self.horizontalLayout_19.addWidget(self.radio_btn_enter)

        self.radio_btn_ctrl_enter = QRadioButton(self.frame_17)
        self.radio_btn_ctrl_enter.setObjectName(u"radio_btn_ctrl_enter")

        self.horizontalLayout_19.addWidget(self.radio_btn_ctrl_enter)

        self.verticalLayout_11.addWidget(self.frame_17, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.extraTopMenu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_15.addWidget(self.label_2)

        self.import_name_list_line_edit = QLineEdit(self.frame_5)
        self.import_name_list_line_edit.setObjectName(u"import_name_list_line_edit")
        self.import_name_list_line_edit.setMinimumSize(QSize(175, 0))
        self.import_name_list_line_edit.setMaximumSize(QSize(260, 16777215))
        self.import_name_list_line_edit.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.import_name_list_line_edit)

        self.btn_import_name_list = QPushButton(self.frame_5)
        self.btn_import_name_list.setObjectName(u"btn_import_name_list")
        self.btn_import_name_list.setMinimumSize(QSize(60, 0))
        self.btn_import_name_list.setMaximumSize(QSize(80, 16777215))
        self.btn_import_name_list.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_import_name_list.setIcon(icon1)
        self.btn_import_name_list.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.btn_import_name_list, 0, Qt.AlignRight)

        self.verticalLayout_11.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_16 = QFrame(self.extraTopMenu)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 40))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.export_tag_name_list_line_edit = QLineEdit(self.frame_16)
        self.export_tag_name_list_line_edit.setObjectName(u"export_tag_name_list_line_edit")
        self.export_tag_name_list_line_edit.setMinimumSize(QSize(175, 0))

        self.horizontalLayout_12.addWidget(self.export_tag_name_list_line_edit)

        self.btn_export_name_list = QPushButton(self.frame_16)
        self.btn_export_name_list.setObjectName(u"btn_export_name_list")
        self.btn_export_name_list.setMinimumSize(QSize(60, 0))
        self.btn_export_name_list.setMaximumSize(QSize(80, 16777215))
        self.btn_export_name_list.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_name_list.setIcon(icon2)
        self.btn_export_name_list.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.btn_export_name_list)

        self.verticalLayout_11.addWidget(self.frame_16, 0, Qt.AlignLeft)

        self.frame_18 = QFrame(self.extraTopMenu)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 40))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_18)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_20.addWidget(self.label_8)

        self.export_chat_group_name_list_line_edit = QLineEdit(self.frame_18)
        self.export_chat_group_name_list_line_edit.setObjectName(u"export_chat_group_name_list_line_edit")
        self.export_chat_group_name_list_line_edit.setMinimumSize(QSize(175, 0))
        self.export_chat_group_name_list_line_edit.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.export_chat_group_name_list_line_edit)

        self.btn_export_chat_group_name_list = QPushButton(self.frame_18)
        self.btn_export_chat_group_name_list.setObjectName(u"btn_export_chat_group_name_list")
        self.btn_export_chat_group_name_list.setMinimumSize(QSize(60, 0))
        self.btn_export_chat_group_name_list.setMaximumSize(QSize(80, 16777215))
        self.btn_export_chat_group_name_list.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_chat_group_name_list.setIcon(icon2)
        self.btn_export_chat_group_name_list.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.btn_export_chat_group_name_list)

        self.verticalLayout_11.addWidget(self.frame_18, 0, Qt.AlignLeft)

        self.verticalLayout_12.addWidget(self.extraTopMenu)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)

        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)

        self.extraColumLayout.addWidget(self.extraContent)

        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon3)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon4)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon5)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
                                         "")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/PyDracula_vertical.png);\n"
                                "background-position: center;\n"
                                "background-repeat: no-repeat;\n"
                                "background-image: url(:/images/images/WeChatMass_vertical.png);")
        self.stackedWidget.addWidget(self.home)
        self.page_friend = QWidget()
        self.page_friend.setObjectName(u"page_friend")
        self.gridLayout = QGridLayout(self.page_friend)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_14 = QFrame(self.page_friend)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 28pt \"Microsoft YaHei UI\";\n"
                                 "color: rgb(85, 255, 127);")

        self.horizontalLayout_9.addWidget(self.label, 0, Qt.AlignHCenter)

        self.gridLayout.addWidget(self.frame_14, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_friend)
        self.wechat = QWidget()
        self.wechat.setObjectName(u"wechat")
        self.wechat.setStyleSheet(
            u"QFrame #frame_sub_1, QFrame#frame_sub_2, QFrame#frame_sub_3, QFrame#frame_sub_4 {border: 2px solid #5D535E; border-radius: 6px;}\n"
            "QTextEdit {background-color: rgb(27, 29, 35); font: 12pt \"Microsoft YaHei UI\";}")
        self.verticalLayout_21 = QVBoxLayout(self.wechat)
        self.verticalLayout_21.setSpacing(3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_sub_1 = QFrame(self.wechat)
        self.frame_sub_1.setObjectName(u"frame_sub_1")
        self.frame_sub_1.setFrameShape(QFrame.StyledPanel)
        self.frame_sub_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_sub_1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_sub_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(4, 4, 4, 3)
        self.single_line_msg_text_edit = QTextEdit(self.frame_6)
        self.single_line_msg_text_edit.setObjectName(u"single_line_msg_text_edit")
        self.single_line_msg_text_edit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.single_line_msg_text_edit.setStyleSheet(u"")
        self.single_line_msg_text_edit.setTabStopDistance(40.000000000000000)

        self.horizontalLayout_7.addWidget(self.single_line_msg_text_edit)

        self.multi_line_msg_text_edit = QTextEdit(self.frame_6)
        self.multi_line_msg_text_edit.setObjectName(u"multi_line_msg_text_edit")
        self.multi_line_msg_text_edit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.multi_line_msg_text_edit.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.multi_line_msg_text_edit)

        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_sub_1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(200, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setStyleSheet(u"font: 500 12pt \"Segoe UI\"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_clear_msg = QPushButton(self.frame_7)
        self.btn_clear_msg.setObjectName(u"btn_clear_msg")
        self.btn_clear_msg.setMinimumSize(QSize(150, 30))
        self.btn_clear_msg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_msg.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_msg.setIcon(icon6)

        self.gridLayout_4.addWidget(self.btn_clear_msg, 0, 0, 1, 1, Qt.AlignHCenter)

        self.horizontalLayout_6.addWidget(self.frame_7)

        self.verticalLayout_21.addWidget(self.frame_sub_1)

        self.frame_sub_2 = QFrame(self.wechat)
        self.frame_sub_2.setObjectName(u"frame_sub_2")
        self.frame_sub_2.setFrameShape(QFrame.StyledPanel)
        self.frame_sub_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_sub_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_sub_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QListWidget {\n"
                                    "    background-color: rgb(27, 29, 35);\n"
                                    "    border-radius: 5px;\n"
                                    "    padding: 3px;\n"
                                    "    border: 1px solid rgb(45, 45, 58);\n"
                                    "	font: 12pt \"Microsoft YaHei UI\";\n"
                                    "}\n"
                                    "\n"
                                    "QListWidget::item {padding: 3px;}\n"
                                    "\n"
                                    "QListWidget QScrollBar:vertical {\n"
                                    "    border: none;\n"
                                    "    background: rgb(52, 59, 72);\n"
                                    "    width: 8px;\n"
                                    "    margin: 21px 0 21px 0;\n"
                                    "    border-radius: 0px;\n"
                                    "}\n"
                                    "\n"
                                    "QListWidget QScrollBar::handle:vertical {background: rgb(189, 147, 249);min-height: 25px;border-radius: 4px;}\n"
                                    "\n"
                                    "QListWidget QScrollBar::add-line:vertical {\n"
                                    "    border: none;\n"
                                    "    background: rgb(55, 63, 77);\n"
                                    "    height: 20px;\n"
                                    "	border-bottom-left-radius: 4px;\n"
                                    "    border-bottom-right-radius: 4px;\n"
                                    "    subcontrol-position: bottom;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "}\n"
                                    "\n"
                                    "QListWidget QScrollBar::sub-line:vertical {\n"
                                    "	border: none;\n"
                                    "    background: rgb(55, 63, 77);\n"
                                    "    height: 20px;\n"
                                    "	border-top-left-radius: 4px;\n"
                                    "    border-top-right-"
                                    "radius: 4px;\n"
                                    "    subcontrol-position: top;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QListWidget QScrollBar::up-arrow:vertical, QListWidget QScrollBar::down-arrow:vertical {background: none;}\n"
                                    "\n"
                                    "QListWidget QScrollBar::add-page:vertical, QListWidget QScrollBar::sub-page:vertical {background: none;}\n"
                                    "\n"
                                    "QMenu {\n"
                                    "    background-color: rgb(37, 39, 48); /* \u83dc\u5355\u80cc\u666f\u8272 */\n"
                                    "    color: rgb(220, 220, 220); /* \u83dc\u5355\u6587\u5b57\u989c\u8272 */\n"
                                    "    border: 1px solid rgb(45, 45, 58); /* \u83dc\u5355\u8fb9\u6846 */\n"
                                    "    font: 12pt \"Segoe UI\"; /* \u5b57\u4f53\u5927\u5c0f\u548c\u7c7b\u578b */\n"
                                    "}\n"
                                    "\n"
                                    "QMenu::item {background-color: transparent; padding: 5px 10px; margin: 1px 1px;}\n"
                                    "\n"
                                    "QMenu::item:selected {background-color: rgb(40, 44, 52);border-left: 2px solid rgb(255, 121, 198);}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_10)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.file_list_widget = QListWidget(self.frame_10)
        self.file_list_widget.setObjectName(u"file_list_widget")
        self.file_list_widget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.file_list_widget.setStyleSheet(u"")
        self.file_list_widget.setDragEnabled(False)

        self.gridLayout_5.addWidget(self.file_list_widget, 0, 0, 1, 1)

        self.horizontalLayout_8.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_sub_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(200, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setStyleSheet(u"font: 500 12pt \"Segoe UI\"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.btn_add_file = QPushButton(self.frame_11)
        self.btn_add_file.setObjectName(u"btn_add_file")
        self.btn_add_file.setMinimumSize(QSize(150, 30))
        self.btn_add_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_file.setIcon(icon7)

        self.verticalLayout_22.addWidget(self.btn_add_file, 0, Qt.AlignHCenter)

        self.btn_clear_file = QPushButton(self.frame_11)
        self.btn_clear_file.setObjectName(u"btn_clear_file")
        self.btn_clear_file.setMinimumSize(QSize(150, 30))
        self.btn_clear_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_clear_file.setIcon(icon6)

        self.verticalLayout_22.addWidget(self.btn_clear_file, 0, Qt.AlignHCenter)

        self.horizontalLayout_8.addWidget(self.frame_11)

        self.verticalLayout_21.addWidget(self.frame_sub_2)

        self.frame_sub_3 = QFrame(self.wechat)
        self.frame_sub_3.setObjectName(u"frame_sub_3")
        self.frame_sub_3.setFrameShape(QFrame.StyledPanel)
        self.frame_sub_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_sub_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_sub_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(4, 4, 4, 3)
        self.name_text_edit = QTextEdit(self.frame_12)
        self.name_text_edit.setObjectName(u"name_text_edit")
        self.name_text_edit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.name_text_edit.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.name_text_edit, 0, 0, 1, 1)

        self.horizontalLayout_10.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_sub_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(200, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setStyleSheet(u"font: 500 12pt \"Segoe UI\"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_13)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame = QFrame(self.frame_13)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(6)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 9)
        self.rb_at_everyone = QRadioButton(self.frame)
        self.rb_at_everyone.setObjectName(u"rb_at_everyone")
        self.rb_at_everyone.setMinimumSize(QSize(150, 0))
        self.rb_at_everyone.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_7.addWidget(self.rb_at_everyone, 0, 0, 1, 1)

        self.verticalLayout_23.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_13)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.rb_add_remark = QRadioButton(self.frame_2)
        self.rb_add_remark.setObjectName(u"rb_add_remark")
        self.rb_add_remark.setMinimumSize(QSize(150, 0))
        self.rb_add_remark.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.rb_add_remark, 0, 0, 1, 1)

        self.verticalLayout_23.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_13)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.btn_clear_name = QPushButton(self.frame_3)
        self.btn_clear_name.setObjectName(u"btn_clear_name")
        self.btn_clear_name.setMinimumSize(QSize(150, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setWeight(QFont.Medium)
        font4.setItalic(False)
        font4.setKerning(True)
        self.btn_clear_name.setFont(font4)
        self.btn_clear_name.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_name.setAutoFillBackground(False)
        self.btn_clear_name.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_clear_name.setIcon(icon6)
        self.btn_clear_name.setAutoDefault(False)

        self.gridLayout_9.addWidget(self.btn_clear_name, 0, 0, 1, 1)

        self.verticalLayout_23.addWidget(self.frame_3)

        self.horizontalLayout_10.addWidget(self.frame_13)

        self.verticalLayout_21.addWidget(self.frame_sub_3)

        self.frame_sub_4 = QFrame(self.wechat)
        self.frame_sub_4.setObjectName(u"frame_sub_4")
        self.frame_sub_4.setStyleSheet(u"QPushButton {\n"
                                       "	border: 2px solid rgb(52, 59, 72);\n"
                                       "	font: 12pt \"Segoe UI\";\n"
                                       "	border-radius: 5px;	\n"
                                       "	background-color: rgb(52, 59, 72);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "	background-color: rgb(40, 44, 52);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "	background-color: rgb(189, 147, 249);\n"
                                       "}")
        self.frame_sub_4.setFrameShape(QFrame.StyledPanel)
        self.frame_sub_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_sub_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_sub_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"font: 550 13pt \"Microsoft YaHei UI\"; color: #f8f8f2")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setSpacing(30)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.task_label = QLabel(self.frame_8)
        self.task_label.setObjectName(u"task_label")
        self.task_label.setMinimumSize(QSize(120, 30))
        self.task_label.setStyleSheet(
            u"border: 1px solid rgb(52, 59, 72); border-radius: 5px; background-color: rgb(52, 59, 72);\n"
            "\n"
            "")

        self.horizontalLayout_14.addWidget(self.task_label)

        self.task_progress_bar = QProgressBar(self.frame_8)
        self.task_progress_bar.setObjectName(u"task_progress_bar")
        self.task_progress_bar.setMinimumSize(QSize(120, 30))
        self.task_progress_bar.setStyleSheet(u"QProgressBar {\n"
                                             "    border: 2px solid #333;\n"
                                             "    border-radius: 5px;\n"
                                             "	text-align: center;\n"
                                             "	background-color: #21252B;\n"
                                             "}\n"
                                             "\n"
                                             "QProgressBar::chunk {\n"
                                             "    border-radius: 3px;\n"
                                             "    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(255, 131, 208), stop:1 rgb(255, 111, 188));\n"
                                             "}\n"
                                             "")
        self.task_progress_bar.setValue(66)
        self.task_progress_bar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_14.addWidget(self.task_progress_bar, 0, Qt.AlignLeft)

        self.btn_export_result = QPushButton(self.frame_8)
        self.btn_export_result.setObjectName(u"btn_export_result")
        self.btn_export_result.setMinimumSize(QSize(120, 30))
        self.btn_export_result.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_result.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/cil-data-transfer-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_result.setIcon(icon8)

        self.horizontalLayout_14.addWidget(self.btn_export_result, 0, Qt.AlignRight)

        self.horizontalLayout_16.addWidget(self.frame_8, 0, Qt.AlignLeft)

        self.frame_20 = QFrame(self.frame_sub_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_send_msg = QPushButton(self.frame_20)
        self.btn_send_msg.setObjectName(u"btn_send_msg")
        self.btn_send_msg.setMinimumSize(QSize(120, 30))
        self.btn_send_msg.setMaximumSize(QSize(16777215, 16777215))
        self.btn_send_msg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send_msg.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/cil-chat-bubble.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_msg.setIcon(icon9)

        self.horizontalLayout_13.addWidget(self.btn_send_msg)

        self.btn_pause_send = QPushButton(self.frame_20)
        self.btn_pause_send.setObjectName(u"btn_pause_send")
        self.btn_pause_send.setMinimumSize(QSize(120, 30))
        self.btn_pause_send.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pause_send.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pause_send.setIcon(icon10)

        self.horizontalLayout_13.addWidget(self.btn_pause_send, 0, Qt.AlignHCenter)

        self.btn_clear_all = QPushButton(self.frame_20)
        self.btn_clear_all.setObjectName(u"btn_clear_all")
        self.btn_clear_all.setMinimumSize(QSize(120, 30))
        self.btn_clear_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_all.setStyleSheet(u"")
        self.btn_clear_all.setIcon(icon6)

        self.horizontalLayout_13.addWidget(self.btn_clear_all)

        self.horizontalLayout_16.addWidget(self.frame_20, 0, Qt.AlignRight)

        self.verticalLayout_21.addWidget(self.frame_sub_4)

        self.stackedWidget.addWidget(self.wechat)

        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)

        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.contentSettings)

        self.horizontalLayout_4.addWidget(self.extraRightBox)

        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)

        self.verticalLayout_6.addWidget(self.bottomBar)

        self.verticalLayout_2.addWidget(self.contentBottom)

        self.appLayout.addWidget(self.contentBox)

        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # if QT_CONFIG(tooltip)
        self.titleLeftApp.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"WeChatMass", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u9065\u9065\u9886\u5148", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_page_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_page_pending.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5b9a", None))
        self.btn_page_msg.setText(QCoreApplication.translate("MainWindow", u"\u7fa4\u53d1\u6d88\u606f", None))
        # if QT_CONFIG(tooltip)
        self.toggleTheme.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.toggleTheme.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u4e3b\u9898", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9762\u677f", None))
        # if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
        # endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6587\u672c\u95f4\u9694", None))
        self.cb_text_interval.setItemText(0, QCoreApplication.translate("MainWindow", u"0.05", None))
        self.cb_text_interval.setItemText(1, QCoreApplication.translate("MainWindow", u"0.1", None))
        self.cb_text_interval.setItemText(2, QCoreApplication.translate("MainWindow", u"0.2", None))
        self.cb_text_interval.setItemText(3, QCoreApplication.translate("MainWindow", u"0.3", None))
        self.cb_text_interval.setItemText(4, QCoreApplication.translate("MainWindow", u"0.4", None))
        self.cb_text_interval.setItemText(5, QCoreApplication.translate("MainWindow", u"0.5", None))
        self.cb_text_interval.setItemText(6, QCoreApplication.translate("MainWindow", u"0.6", None))
        self.cb_text_interval.setItemText(7, QCoreApplication.translate("MainWindow", u"0.7", None))
        self.cb_text_interval.setItemText(8, QCoreApplication.translate("MainWindow", u"0.8", None))
        self.cb_text_interval.setItemText(9, QCoreApplication.translate("MainWindow", u"0.9", None))
        self.cb_text_interval.setItemText(10, QCoreApplication.translate("MainWindow", u"1.0", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6587\u4ef6\u95f4\u9694", None))
        self.cb_file_interval.setItemText(0, QCoreApplication.translate("MainWindow", u"0.5", None))
        self.cb_file_interval.setItemText(1, QCoreApplication.translate("MainWindow", u"1.0", None))
        self.cb_file_interval.setItemText(2, QCoreApplication.translate("MainWindow", u"1.5", None))
        self.cb_file_interval.setItemText(3, QCoreApplication.translate("MainWindow", u"2.0", None))
        self.cb_file_interval.setItemText(4, QCoreApplication.translate("MainWindow", u"2.5", None))
        self.cb_file_interval.setItemText(5, QCoreApplication.translate("MainWindow", u"3.0", None))
        self.cb_file_interval.setItemText(6, QCoreApplication.translate("MainWindow", u"3.5", None))
        self.cb_file_interval.setItemText(7, QCoreApplication.translate("MainWindow", u"4.0", None))
        self.cb_file_interval.setItemText(8, QCoreApplication.translate("MainWindow", u"4.5", None))
        self.cb_file_interval.setItemText(9, QCoreApplication.translate("MainWindow", u"5.0", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u52a8\u753b\u542f\u52a8", None))
        self.radio_btn_animate_true.setText(QCoreApplication.translate("MainWindow", u"\u662f     ", None))
        self.radio_btn_animate_false.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5fae\u4fe1\u53d1\u9001\u6d88\u606f", None))
        self.radio_btn_enter.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.radio_btn_ctrl_enter.setText(QCoreApplication.translate("MainWindow", u"Ctrl + Enter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u597d\u53cb\u540d\u5355", None))
        self.btn_import_name_list.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u597d\u53cb\u540d\u5355", None))
        # if QT_CONFIG(tooltip)
        self.export_tag_name_list_line_edit.setToolTip(QCoreApplication.translate("MainWindow",
                                                                                  u"\u82e5\u83b7\u53d6\u5168\u90e8\u597d\u53cb\u540d\u5355\uff0c\u5219\u8f93\u5165\u5168\u90e8",
                                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.export_tag_name_list_line_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u5904\u8f93\u5165\u6807\u7b7e", None))
        self.btn_export_name_list.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u7fa4\u804a\u540d\u5355", None))
        # if QT_CONFIG(tooltip)
        self.export_chat_group_name_list_line_edit.setToolTip(QCoreApplication.translate("MainWindow",
                                                                                         u"\u82e5\u83b7\u53d6\u5168\u90e8\u597d\u53cb\u540d\u5355\uff0c\u5219\u8f93\u5165\u5168\u90e8",
                                                                                         None))
        # endif // QT_CONFIG(tooltip)
        self.export_chat_group_name_list_line_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u53f3\u4fa7\u5bfc\u51fa\u6309\u94ae\u5373\u53ef",
                                       None))
        self.btn_export_chat_group_name_list.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow",
                                                         u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "hr { height: 1px; border-width: 0; }\n"
                                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                                         "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ff79c6;\">WeChatMassTool</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u57fa\u4e8ePySide6 \u548c Python \u6784\u5efa\u7684\u5fae\u4fe1\u7fa4\u53d1\u5de5\u5177\uff0c\u63d0\u4f9b\u7b80"
                                                         "\u5355\u9ad8\u6548\u7684\u7fa4\u53d1\u6d88\u606f\u529f\u80fd\u3002\u5de5\u5177\u6837\u5f0f\u57fa\u4e8e </span><span style=\" font-weight:700; color:#bd93f9;\">PyDracula</span>\u3002</p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u5982\u4f55\u83b7\u53d6</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">\u5173\u6ce8\u516c\u4f17\u53f7\uff1a</span><span style=\" font-weight:700; color:#bd93f9;\">\u5c0f\u83dc\u7684Python\u6742\u8d27\u94fa</span><span style=\" font-size:9pt; color:#ffffff;\"><br />\u56de\u590d\uff1a</span><span style=\" font-size:9pt; font-weight:700; color:#ff79c6;\">\u5fae\u4fe1\u7fa4\u53d1</span><span style=\" font-size:9pt; color:#ffffff;\">\uff0c\u5373\u53ef\u83b7\u53d6</span></p>\n"
                                                         ""
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u5982\u4f55\u4f7f\u7528</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">\u53cc\u51fb\u6b64\u5904\uff0c\u5373\u53ef\u6253\u5f00\u89c6\u9891\u6559\u7a0b</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u6280\u672f\u6808</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u4f7f\u7528 PySide6 \u8fdb\u884c UI \u5f00\u53d1\uff0cPython \u811a\u672c\u8fdb\u884c\u540e"
                                                         "\u7aef\u903b\u8f91\u5904\u7406\u3002</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u5f00\u53d1\u8005</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#bd93f9;\">\u7531\u5c0f\u83dc\u7cbe\u5fc3\u5f00\u53d1</span></p></body></html>",
                                                         None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow",
                                                               u"<html><head/><body><p><span style=\"font-family:'Microsoft YaHei UI'; color:#ff79c6;\">WeChatMassTool</span> - \u57fa\u4e8ePython\u5f00\u53d1\u7684\u5fae\u4fe1\u7fa4\u53d1\u5de5\u5177.</p></body></html>",
                                                               None))
        # if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
        # endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u6b64\u9875\u9762\u5373\u5c06\u6dfb\u52a0\u670b\u53cb\u5708\u70b9\u8d5e\u529f\u80fd\u3002",
                                                      None))
        self.single_line_msg_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                     u"\u5728\u6b64\u5904\u8f93\u5165\u6d88\u606f\uff0c\u4e00\u884c\u4e3a\u4e00\u6761\u6d88\u606f",
                                                                                     None))
        self.multi_line_msg_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                    u"\u5728\u6b64\u5904\u8f93\u5165\u6d88\u606f\uff0c\u4e00\u5171\u4e3a\u4e00\u6761\u6d88\u606f",
                                                                                    None))
        self.btn_clear_msg.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u5165", None))
        self.btn_add_file.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.btn_clear_file.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6587\u4ef6", None))
        self.name_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u5728\u6b64\u8f93\u5165\u597d\u53cb\u6635\u79f0\uff0c\u4e00\u884c\u4e3a\u4e00\u4e2a\u597d\u53cb",
                                                                          None))
        self.rb_at_everyone.setText(QCoreApplication.translate("MainWindow", u"@\u6240\u6709\u4eba", None))
        self.rb_add_remark.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5907\u6ce8", None))
        self.btn_clear_name.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u5165", None))
        self.task_label.setText(QCoreApplication.translate("MainWindow", u"\u9700\u53d1\u9001\uff1a0 \u4f4d", None))
        self.task_progress_bar.setFormat(QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u6210 %p%", None))
        self.btn_export_result.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u7ed3\u679c", None))
        self.btn_send_msg.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u53d1\u9001", None))
        self.btn_pause_send.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u53d1\u9001", None))
        self.btn_clear_all.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u5168\u90e8", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: \u5c0f\u83dc", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

# -*- coding: utf-8 -*-
# Name:         config.py
# Author:       小菜
# Date:         2024/3/22 15:19
# Description:

TUTORIAL_LINK = 'https://www.bilibili.com/video/BV1v1421z7Rq'


class AnimateConfig:
    SECTION = 'DEFAULT'
    OPTION = 'animate_on_startup'


class WeChatConfig:
    WeChat_PROCESS_NAME = 'WeChat.exe'
    APP_NAME = 'WeChatMassTool'
    APP_PROCESS_NAME = 'WeChatMassTool.exe'
    APP_LOCK_NAME = 'WeChatMassTool.lock'
    WINDOW_NAME = '微信'
    WINDOW_CLASSNAME = 'WeChatMainWndForPC'


class ViewConfig:
    # APP SETTINGS
    MENU_WIDTH = 180
    LEFT_BOX_WIDTH = 360
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500


class DarkConfig:
    QSS_FILE = 'views/resources/themes/py_dracula_dark.qss'

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: rgb(40, 44, 52);
        """

    # MANUAL STYLES
    MANUAL_STYLES = {
        'wechat': '''QTextEdit{background-color: rgb(27, 29, 35); font: 12pt "Microsoft YaHei UI";} 
                    QFrame #frame_sub_1, 
                    QFrame#frame_sub_2, 
                    QFrame#frame_sub_3, 
                    QFrame#frame_sub_4 {
                        border: 2px solid #5D535E;border-radius: 6px;
                    }''',
        'file_list_widget': '''QListWidget {
                                    background-color: rgb(27, 29, 35);
                                    border-radius: 5px;
                                    padding: 3px;
                                    border: 1px solid rgb(45, 45, 58);
                                    font: 12pt "Microsoft YaHei UI";
                                    color: #f8f8f2;
                                }'''

    }


class LightConfig:
    QSS_FILE = 'views/resources/themes/py_dracula_light.qss'

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: #495474;"
    BTN_RIGHT_BOX_COLOR = "background-color: #495474;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

    # MANUAL STYLES
    MANUAL_STYLES = {
        'wechat': '''QTextEdit{
                        background-color: #6272a4; 
                        font: 12pt "Microsoft YaHei UI";
                    } 
                    QFrame#frame_sub_1, 
                    QFrame#frame_sub_2, 
                    QFrame#frame_sub_3, 
                    QFrame#frame_sub_4 {
                        border: 2px solid #627282;
                        border-radius: 6px;
                    }''',
        'file_list_widget': '''QListWidget {
                                    background-color: #6272a4;
                                    border-radius: 5px;
                                    padding: 3px;
                                    border: 1px solid rgb(45, 45, 58);
                                    font: 12pt "Microsoft YaHei UI";
                                    color: #f8f8f2;
                                }'''
    }


class IntervalConfig:
    BASE_INTERVAL = 0.1  # 基础间隔（秒）
    SEND_TEXT_INTERVAL = 0.05  # 发送文本间隔（秒）
    SEND_FILE_INTERVAL = 0.25  # 发送文件间隔（秒）
    MAX_SEARCH_SECOND = 0.1
    MAX_SEARCH_INTERVAL = 0.05

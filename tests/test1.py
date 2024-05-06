# -*- coding: utf-8 -*-
# Name:         test1.py
# Author:       小菜
# Date:         2024/4/18 15:13
# Description:


# 等待，以便观察到没有窗口的情况
from utils import get_specific_process

print(get_specific_process('cmd.exe'))

import win32gui
import win32con
import win32process


def check_window(hwnd, _):
    """检查窗口类名并获取窗口标题"""
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    if 'sekiro.bat' in win32gui.GetWindowText(hwnd):
        title = win32gui.GetWindowText(hwnd)
        win32gui.ShowWindow(win32gui.FindWindow(None, title), win32con.SW_HIDE)


def enum_windows():
    """枚举所有窗口并检查特定进程的窗口"""
    win32gui.EnumWindows(check_window, None)


# enum_windows()

with open(r'C:\Users\plan\Desktop\WeChatMassTool\123.txt', 'r', encoding='ascii') as f:
    print(f.read())

import chardet
# 首先检测文件的编码
with open(r'C:\Users\plan\Desktop\WeChatMassTool\123.txt', 'rb') as file:
    raw_data = file.read(4096)  # 或者更多，取决于文件大小
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(encoding)
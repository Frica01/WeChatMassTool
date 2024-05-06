# -*- coding: utf-8 -*-
# Name:         utils.py
# Author:       小菜
# Date:         2024/4/1 00:00
# Description:

import ctypes
import os.path
import sys
from ctypes import wintypes

import chardet
import psutil
import win32clipboard
import win32con
import win32gui


def get_specific_process(proc_name: str = 'WeChat.exe') -> bool:
    """获取指定进程是否存在"""
    return any(proc.name() == proc_name for proc in psutil.process_iter(attrs=['name']))


def read_file(file: str):
    try:
        # 检测文件的编码
        with open(file, 'rb') as f:
            result = chardet.detect(f.read(4096))
            encoding = result['encoding']
        with open(file, encoding=encoding) as f:
            return f.read().split('\n')
    except (FileNotFoundError, FileExistsError):
        ...
    finally:
        ...


def copy_files_to_clipboard(file_paths: list):
    # 定义所需的 Windows 结构和函数
    CF_HDROP = 15

    class DROPFILES(ctypes.Structure):
        _fields_ = [("pFiles", wintypes.DWORD),
                    ("pt", wintypes.POINT),
                    ("fNC", wintypes.BOOL),
                    ("fWide", wintypes.BOOL)]

    offset = ctypes.sizeof(DROPFILES)
    length = sum(len(p) + 1 for p in file_paths) + 1
    size = offset + length * ctypes.sizeof(wintypes.WCHAR)
    buf = (ctypes.c_char * size)()
    df = DROPFILES.from_buffer(buf)
    df.pFiles, df.fWide = offset, True
    for path in file_paths:
        path = path.replace('/', '\\')
        array_t = ctypes.c_wchar * (len(path) + 1)
        path_buf = array_t.from_buffer(buf, offset)
        path_buf.value = path
        offset += ctypes.sizeof(path_buf)
    buf[offset:offset + ctypes.sizeof(wintypes.WCHAR)] = b'\0\0'

    # 将数据放入剪切板
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(CF_HDROP, buf)
    win32clipboard.CloseClipboard()


def minimize_wechat(class_name, name):
    """
    结束时候最小化微信窗口

    Args:
        name(str):  进程名
        class_name(str):  进程class_name

    Returns:

    """
    hwnd = win32gui.FindWindow(class_name, name)
    if win32gui.IsWindowVisible(hwnd):
        # 展示窗口，以下几行代码都可以唤醒窗口
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)


def wake_up_window(class_name, name):
    """
    唤醒微信窗口

    Args:
        name(str):  进程名
        class_name(str):  进程class_name

    Returns:

    """
    if hwnd := win32gui.FindWindow(class_name, name):
        # 展示窗口
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWDEFAULT)


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

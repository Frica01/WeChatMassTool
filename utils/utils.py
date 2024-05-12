# -*- coding: utf-8 -*-
# Name:         utils.py
# Author:       小菜
# Date:         2024/4/1 00:00
# Description:

import ctypes
import os
import sys
from ctypes import wintypes
from configparser import ConfigParser
from pathlib import Path

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


def write_file(file: str, data: list):
    try:
        with open(file, encoding='utf-8', mode='w') as f:
            f.write("\n".join(data))
    except (FileNotFoundError, FileExistsError):
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
        win32gui.SendMessage(hwnd, win32con.WM_CLOSE, 0, 0)


def wake_up_window(class_name, name):
    """
    唤醒微信窗口

    Args:
        name(str):  进程名
        class_name(str):  进程class_name

    Returns:

    """
    if hwnd := win32gui.FindWindow(class_name, name):
        # 回复窗口
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        # 尝试将窗口置前
        try:
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            print(f"尝试将窗口置前时出错: {e}")


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_user_config_dir(app_name):
    # 根据操作系统不同，返回用户的配置目录
    if os.name == "nt":
        # Windows
        return Path.home() / "AppData" / "Local" / app_name
    else:
        # Unix-like
        return Path.home() / ".config" / app_name


def create_default_config(config_path):
    # 创建ConfigParser对象
    config = ConfigParser()
    # 创建一个新的config文件，并添加一个section
    config['DEFAULT'] = {}
    # 添加一个字段 animation=False 到 DEFAULT section
    config.set('DEFAULT', 'animate_on_startup', 'True')
    # 将配置项写入文件
    with open(config_path, 'w') as configfile:
        config.write(configfile)


def get_config(app_name, section='DEFAULT', option=None):
    # 使用示例
    config_dir = get_user_config_dir(app_name)
    config_path = config_dir / "config.ini"

    if not config_dir.exists():
        config_dir.mkdir(parents=True, exist_ok=True)  # exist_ok 避免重复创建时的错误

    # 确保配置文件存在，如果不存在则创建或复制默认配置
    if not config_path.exists():
        create_default_config(config_path)

    # 读取配置文件
    config = ConfigParser()
    config.read(config_path)
    return config.getboolean(section, option=option)


def write_config(app_name, section, option, value):
    # 使用示例
    config_dir = get_user_config_dir(app_name)
    config_path = config_dir / "config.ini"

    # 读取或创建 ConfigParser 对象
    config = ConfigParser()
    if not config.read(config_path):
        create_default_config(config_path=config_path)

    # 设置或更新配置项的值
    config.set(section, option, value)

    # 将更新后的配置写回文件
    with open(config_path, 'w') as configfile:
        config.write(configfile)

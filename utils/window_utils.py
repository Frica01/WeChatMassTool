# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/12 下午5:22
# @Name   : window_utils.py
import os
import subprocess
import winreg

import win32con
import win32gui

from utils.process_utils import get_wechat_path


def minimize_wechat(class_name, name):
    """
    关闭Windows窗口

    Args:
        name(str):  进程名
        class_name(str):  进程class_name

    Returns:

    """
    hwnd = win32gui.FindWindow(class_name, name)
    if win32gui.IsWindowVisible(hwnd):
        win32gui.SendMessage(hwnd, win32con.WM_CLOSE, 0, 0)


def wake_up_window(process_name: str = 'Weixin.exe') -> bool:
    # 方法1：从注册表获取（如果已安装但未运行）
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Weixin"
        )
        path, _ = winreg.QueryValueEx(key, "InstallLocation")
        winreg.CloseKey(key)
        exe_path = os.path.join(path, process_name)
        if os.path.exists(exe_path):
            subprocess.Popen(exe_path)
            return True

    except FileNotFoundError:
        pass

    # 方法2：检查微信进程（如果正在运行）
    if exe_path := get_wechat_path(proc_name=process_name):
        subprocess.Popen(exe_path)
        return True

    return False

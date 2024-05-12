# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/12 下午5:22
# @Name   : clipboard_utils.py

import ctypes
import win32clipboard
from ctypes import wintypes
from typing import Iterable


def copy_files_to_clipboard(file_paths):
    """
    将一系列文件路径复制到Windows剪切板。这允许用户在其他应用程序中，如文件资源管理器中粘贴这些文件。

    Args:
        file_paths (Iterable): 一个包含文件路径的可迭代对象，每个路径都是一个字符串。

    Returns:
        None: 函数没有返回值，但会修改系统的剪切板内容。
    """
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

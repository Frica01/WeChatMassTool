# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/12 下午5:22
# @Name   : clipboard_utils.py

import ctypes
import os
import time
from ctypes import wintypes
from typing import (Iterable, Callable, List)

import win32clipboard


def retry_on_failure(max_retries: int = 5):
    """
    一个装饰器，用于在失败时重试执行被装饰的函数。

    Args:
        max_retries (int): 最大重试次数。

    Returns:
        Callable: 包装后的函数。
    """

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    if func(*args, **kwargs):
                        return True
                except Exception as e:
                    time.sleep(.05)
                    print(f"Attempt {attempt + 1} failed: {e}")
            return False

        return wrapper

    return decorator


def set_clipboard_data(fmt: int, buf: ctypes.Array) -> bool:
    """
    将数据设置到Windows剪切板中。

    Args:
        fmt (int): 数据格式，例如 win32clipboard.CF_HDROP。
        buf (ctypes.Array): 要设置到剪切板的数据。

    Returns:
        bool: 操作成功返回 True，否则返回 False。
    """
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(fmt, buf)
        return True
    except Exception as e:
        print(f"Error setting clipboard data: {e}")
        return False
    finally:
        win32clipboard.CloseClipboard()


def get_clipboard_files() -> List[str]:
    """
    获取剪切板中的文件路径列表。

    Returns:
        List[str]: 包含剪切板中文件路径的列表，如果没有文件路径或操作失败，返回空列表。
    """
    try:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_HDROP):
            return list(win32clipboard.GetClipboardData(win32clipboard.CF_HDROP))
        else:
            return list()
    finally:
        win32clipboard.CloseClipboard()


@retry_on_failure(max_retries=5)
def validate_clipboard_files(file_paths: Iterable[str], fmt: int, buf: ctypes.Array) -> bool:
    """
    验证剪切板中的文件路径是否与给定的文件路径一致。

    Args:
        file_paths (Iterable): 一个包含文件路径的可迭代对象，每个路径都是一个字符串。
        fmt (int): 数据格式，例如 win32clipboard.CF_HDROP。
        buf (ctypes.Array): 要验证的剪切板数据。

    Returns:
        bool: 如果剪切板中的文件路径与给定的文件路径一致，则返回 True

    Raises:
        ValueError: 如果剪切板文件路径与给定文件路径不一致。
    """
    # 设置文件到剪切板
    set_clipboard_data(fmt, buf)
    # 验证剪切板中的文件路径是否与给定的文件路径一致
    if set(get_clipboard_files()) == set(file_paths):
        return True
    raise ValueError("剪切板文件路径不对哇！")


def copy_files_to_clipboard(file_paths: Iterable[str]) -> bool:
    """
    将一系列文件路径复制到Windows剪切板。这允许用户在其他应用程序中，如文件资源管理器中粘贴这些文件。

    Args:
        file_paths (Iterable): 一个包含文件路径的可迭代对象，每个路径都是一个字符串。

    Returns:
        bool: 如果成功将文件路径复制到剪切板，则返回 True，否则返回 False
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
        path = os.path.normpath(path)
        array_t = ctypes.c_wchar * (len(path) + 1)
        path_buf = array_t.from_buffer(buf, offset)
        path_buf.value = path
        offset += ctypes.sizeof(path_buf)
    buf[offset:offset + ctypes.sizeof(wintypes.WCHAR)] = b'\0\0'

    # 验证文件是否成功复制到剪切板
    return validate_clipboard_files([os.path.normpath(file) for file in file_paths], CF_HDROP, buf=buf)

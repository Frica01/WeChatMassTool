# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/12 下午5:21
# @Name   : file_io.py

import os
import sys

import chardet


def read_file(file: str):
    """
    读取指定文件的内容，并返回一个由文件各行组成的列表。

    Args:
        file (str): 要读取的文件的路径。

    Returns:
        list: 文件内容的列表，其中每个元素代表文件的一行。

    Raises:
        FileNotFoundError: 当指定的文件不存在时抛出。
        FileExistsError: 当文件无法访问时抛出。
    """
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
    """
    将提供的数据写入指定文件。数据应为字符串列表，函数会将其合并为单个字符串并写入文件。

    Args:
        file (str): 要写入的文件的路径。
        data (list): 要写入文件的字符串列表，列表中的每个元素代表文件的一行。

    Raises:
        FileNotFoundError: 当指定的文件不存在时抛出。
        FileExistsError: 当文件无法访问时抛出。
    """
    try:
        with open(file, encoding='utf-8', mode='w') as f:
            f.write("\n".join(data))
    except (FileNotFoundError, FileExistsError):
        ...


def get_resource_path(relative_path):
    """
    根据提供的相对路径，返回资源的绝对路径。这个函数特别适用于打包后的应用程序中资源的路径处理。

    Args:
        relative_path (str): 资源的相对路径。

    Returns:
        str: 资源的绝对路径。
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

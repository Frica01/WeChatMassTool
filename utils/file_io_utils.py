# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/12 下午5:21
# @Name   : file_io_utils.py

import os
import sys
import tempfile
import time
from typing import Optional

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
            return [line for line in f.read().split('\n') if line.strip()]
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
        # 确保文件的父目录存在。如果目录不存在，则递归创建该目录
        directory = os.path.dirname(file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # 创建文件
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


def get_pid():
    """
    返回当前进程id

    Returns:
        int: 进程id

    Examples:
        >>> get_pid()
    """
    return os.getpid()


def get_temp_file_path(file_name: Optional[str] = None):
    """
    获取临时文件路径

    该函数接收一个相对路径，并返回在系统临时目录中的完整路径

    Args:
        file_name (Optional[str]): 文件名

    Returns:
        str: 系统临时目录中该相对路径的完整路径

    Examples:
        >>> get_temp_file_path('example.txt')
    """
    if file_name:
        return os.path.join(tempfile.gettempdir(), file_name)
    return tempfile.gettempdir()


def file_exists(file_path):
    """
    判断文件是否存在

    Args:
        file_path (str): 文件的路径

    Returns:
        bool: 如果文件存在返回 True，否则返回 False

    Examples:
        >>> file_exists('example.txt')
    """
    return os.path.exists(file_path)


def delete_file(file_path):
    """
    删除临时文件

    该函数接收一个相对路径，并删除在系统临时目录中的对应文件

    Args:
        file_path(str): 文件路径

    Returns:
        bool: 如果文件成功删除返回 True，否则返回 False

    Examples:
        >>> delete_file('example.txt')
    """

    try:
        os.remove(file_path)
    except FileNotFoundError:
        return False


def delete_old_files_with_extension(directory, days=3, file_extension='.tmp'):
    """
    删除指定文件夹中超过指定天数前创建的所有文件

    Args:
        directory (str): 文件夹的路径
        days (int): 删除几天前创建的文件，默认为3天前
        file_extension (str): 需要删除的文件后缀，默认为'.tmp'

    Returns:
        None

    Examples:
        >>> delete_old_files_with_extension('路径', days=1)
    """
    if not file_exists(directory):
        print(f"'{directory}' 文件夹不存在")
        return

    # 计算时间阈值
    cutoff = time.time() - days * 86400  # 86400秒等于1天

    # 遍历文件夹
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(file_extension):
                file_path = os.path.join(root, file_name)
                # 获取文件的创建时间
                file_ctime = os.path.getctime(file_path)
                # 如果文件的创建时间早于时间阈值，则删除文件
                if file_ctime < cutoff:
                    print(f"Deleting file: {file_path}")  # 打印出删除的文件路径
                    delete_file(file_path)

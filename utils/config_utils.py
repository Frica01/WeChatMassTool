# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/12 下午5:22
# @Name   : config_utils.py

import os
from configparser import ConfigParser
from pathlib import Path


def get_user_config_dir(app_name):
    """
    根据操作系统类型获取用户的配置文件目录。

    Args:
        app_name(str): 应用程序的名称，用于创建或查找配置目录。

    Returns:
        一个Path对象，指向用户的配置目录
    """
    # 根据操作系统不同，返回用户的配置目录
    if os.name == "nt":
        # Windows
        return Path.home() / "AppData" / "Local" / app_name
    else:
        # Unix-like
        return Path.home() / ".config" / app_name


def create_default_config(config_path):
    """
    在指定路径创建一个默认配置文件。

    Args:
        config_path(str): 配置文件的路径。

    Returns:
        None
    """
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
    """
    获取指定应用程序配置项的值。

    Args:
        app_name(str): 应用程序的名称。
        section(str): 配置文件中的节名称。
        option(str): 要检索的配置项名称。

    Returns:
        配置项的值（bool）。
    """

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
    """
    在配置文件中写入或更新一个配置项。

    Args:
        app_name(str): 应用程序的名称。
        section(str): 配置文件中的节名称。
        option(str): 配置项的名称。
        value(str): 配置项的新值。

    Returns:
        None
    """

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

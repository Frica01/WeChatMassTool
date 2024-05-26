# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/27 上午12:30
# @Name   : browser_utils.py

import webbrowser


def open_webpage(url):
    """
    使用默认浏览器打开指定的URL.

    Args:
        url(str): 要打开的网页URL

    Returns:

    Examples:
        >>> open_webpage('https://www.bilibili.com/video/BV1v1421z7Rq')

    """
    try:
        webbrowser.open(url)
        print(f"Successfully opened {url}")
    except Exception as e:
        print(f"Failed to open {url}: {e}")

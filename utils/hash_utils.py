# -*- coding: utf-8 -*-
# Name:         hash_utils.py
# Author:       小菜
# Date:         2024/5/24 上午02:18
# Description:

import hashlib


def get_file_sha256(file_path):
    """
    获取文件的 SHA-256 哈希值

    Args:
        file_path (str): 文件的路径

    Returns:
        str: 文件的 SHA-256 哈希值

    Examples:
        >>> get_file_sha256('example.txt')
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # 逐块读取文件，防止文件过大导致内存不足
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

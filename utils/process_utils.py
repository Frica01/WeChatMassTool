# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/12 下午5:31
# @Name   : process_utils.py


import wmi


def get_specific_process(proc_name: str = 'WeChat.exe') -> bool:
    """获取指定进程是否存在"""
    return any(process.Name == proc_name for process in wmi.WMI().Win32_Process(Name=proc_name))

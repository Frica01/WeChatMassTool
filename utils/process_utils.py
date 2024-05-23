# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024/5/12 下午5:31
# @Name   : process_utils.py

from typing import Union

import wmi


def get_specific_process(proc_name: str = 'WeChat.exe') -> bool:
    """获取指定进程是否存在"""
    return any(process.Name == proc_name for process in wmi.WMI().Win32_Process(Name=proc_name))


def is_process_running(pid: Union[int, str], proc_name: str):
    """使用 WMI 检查给定的 PID 是否在运行状态"""
    # None 表示运行中, 判断进程是否运行切是否为
    return any(
        process.ExecutionState is None and process.Name == proc_name for process in
        wmi.WMI().Win32_Process(ProcessId=pid)
    )

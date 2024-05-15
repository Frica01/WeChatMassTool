# -*- coding: utf-8 -*-
# Name:         model_main.py
# Author:       小菜
# Date:         2024/4/1 00:00
# Description:

from typing import Dict
from collections import defaultdict
from PySide6.QtCore import (QObject, QRunnable, QThreadPool, Slot, Signal)

from utils import (WxOperation, write_file)
from models import RecordGeneratorModel


class TaskRunnable(QRunnable):
    def __init__(self, func, task_id, *args, **kwargs):
        super().__init__()
        self.func = func
        self.task_id = task_id
        self.args = args
        self.kwargs = kwargs
        self.toggleTaskStatusSignal = kwargs.get('toggleTaskStatusSignal')

    def run(self):
        try:
            self.execute_task()
        except Exception as e:
            self.handle_error(e)
        finally:
            self.toggleTaskStatusSignal.emit(self.task_id)

    def execute_task(self):
        # 将由子类实现具体任务
        pass

    def handle_error(self, error):
        # 可以在这里处理或记录错误
        print(f"Error in {self.task_id}: {error}")


class SendMessageTask(TaskRunnable):
    def execute_task(self):
        # 实现发送消息的逻辑
        message_info = self.kwargs.get('message_info')
        check_pause = self.kwargs.get('check_pause')
        updatedProgressSignal = self.kwargs.get('updatedProgressSignal')
        recordExecInfoSignal = self.kwargs.get('recordExecInfoSignal')

        names = message_info.pop('names')
        exec_info_map = dict()
        for idx, name in enumerate(names):
            check_pause()
            try:
                exec_info_map.update(
                    {
                        '昵称': name,
                        '文本': '\n'.join(message_info.get('msgs', str())),
                        '文件': '\n'.join(message_info.get('file_paths', str())),
                        '状态': '成功'
                    }
                )
                self.func(name, **message_info)
            except (ValueError, TypeError, AssertionError, NameError) as e:
                exec_info_map.update(
                    {
                        '状态': '失败',
                        '备注': str(e)
                    }
                )
            finally:
                recordExecInfoSignal.emit(exec_info_map)
                updatedProgressSignal.emit(idx + 1, len(names))  # 通知控制器任务完成


class GetNameListTask(TaskRunnable):
    def execute_task(self):
        tag = self.kwargs.get('tag')
        file_path = self.kwargs.get('file_path')
        exportNameListSignal = self.kwargs.get('exportNameListSignal')
        try:
            result = self.func(tag)
            write_file(file_path, data=result)
            exportNameListSignal.emit(True, '文件导出成功')
        except LookupError:
            exportNameListSignal.emit(False, f'找不到 {tag} 标签')


class ModelMain(QObject):
    toggleTaskStatusSignal = Signal(str)
    recordExecInfoSignal = Signal(dict)
    exportNameListSignal = Signal(bool, str)

    def __init__(self):
        super().__init__()
        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(1)
        #
        self.record = RecordGeneratorModel()
        self.wx = WxOperation()
        #
        self.task_status_map: Dict[str, bool] = defaultdict()  # 用于存放不同任务的状态
        self.toggleTaskStatusSignal.connect(self.change_task_status)
        self.recordExecInfoSignal.connect(self.record_exec_info)

    def __del__(self):
        self.record.cleanup()

    def export_name_list(self, tag, file_path):
        """导出标签好友名单"""
        task_id = 'name_list'
        if self.task_status_map.get(task_id):
            return
        self.toggleTaskStatusSignal.emit(task_id)

        runnable = GetNameListTask(
            self.wx.get_friend_list,
            task_id=task_id,
            tag=None if tag == '全部' else tag,
            file_path=file_path,
            toggleTaskStatusSignal=self.toggleTaskStatusSignal,
            exportNameListSignal=self.exportNameListSignal
        )
        self.thread_pool.start(runnable)

    def send_wechat_message(self, message_info: dict, check_pause, updatedProgressSignal):
        """发送微信消息"""
        task_id = 'send_msg'
        if self.task_status_map.get(task_id):
            return
        self.toggleTaskStatusSignal.emit(task_id)

        # 处理数据
        message_info = self.process_message_info(message_info=message_info)
        runnable = SendMessageTask(
            self.wx.send_msg,
            task_id=task_id,
            check_pause=check_pause,
            message_info=message_info,
            updatedProgressSignal=updatedProgressSignal,
            toggleTaskStatusSignal=self.toggleTaskStatusSignal,
            recordExecInfoSignal=self.recordExecInfoSignal
        )
        self.thread_pool.start(runnable)

    @staticmethod
    def process_message_info(message_info):
        # 处理昵称
        message_info['names']: list = message_info['names'].split()
        message_info['names'].extend(message_info.pop('name_list', list()))
        # 处理消息
        msg_list = list()
        if signal_text := message_info.pop('single_text', None):
            msg_list.extend(signal_text.split('\n'))
        if multi_text := message_info.pop('multi_text', None):
            msg_list.append(multi_text)
        message_info['msgs'] = msg_list
        return message_info

    @Slot(dict)
    def record_exec_info(self, item):
        # print('record item ==>', item)
        self.record.record_exec_result(item)

    @Slot(bool)
    def change_task_status(self, task_id):
        self.task_status_map[task_id] = not self.task_status_map.get(task_id)

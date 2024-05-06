# -*- coding: utf-8 -*-
# Name:         model_main.py
# Author:       小菜
# Date:         2024/4/1 00:00
# Description:

from PySide6.QtCore import (QObject, QRunnable, QThreadPool, Slot, Signal)

from utils import WxOperation
from models import RecordGeneratorModel


class TaskRunnable(QRunnable):
    def __init__(self, func, message_info, **kwargs):
        super().__init__()
        self.func = func
        self.message_info = message_info
        self.check_pause = kwargs.get('check_pause')
        self.toggleTaskStatusSignal = kwargs.get('toggleTaskStatusSignal')
        self.updatedProgressSignal = kwargs.get('updatedProgressSignal')
        self.recordExecInfoSignal = kwargs.get('recordExecInfoSignal')

    def run(self):
        exec_info_map = dict()
        names = self.message_info.pop('names')
        for idx, name in enumerate(names):
            self.check_pause()
            try:
                exec_info_map.update(
                    {
                        '昵称': name,
                        '文本': '\n'.join(self.message_info.get('msgs', str())),
                        '文件': '\n'.join(self.message_info.get('file_paths', str())),
                        '状态': '成功'
                    }
                )
                self.func(name, **self.message_info)
            except (ValueError, TypeError, AssertionError, NameError) as e:
                exec_info_map.update(
                    {
                        '状态': '失败',
                        '备注': str(e)
                    }
                )
            finally:
                self.recordExecInfoSignal.emit(exec_info_map)
                self.updatedProgressSignal.emit(idx + 1, len(names))  # 通知控制器任务完成
        self.toggleTaskStatusSignal.emit(True)


class ModelMain(QObject):
    toggleTaskStatusSignal = Signal(bool)
    recordExecInfoSignal = Signal(dict)

    def __init__(self):
        super().__init__()
        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(1)
        #
        self.record = RecordGeneratorModel()
        self.wx = WxOperation()
        #
        self.task_status: bool = False
        self.toggleTaskStatusSignal.connect(self.change_task_status)
        self.recordExecInfoSignal.connect(self.record_exec_info)

    def __del__(self):
        self.record.cleanup()

    def send_wechat_message(self, message_info: dict, check_pause, updatedProgressSignal):
        # print('self.task_status ==>', self.task_status)
        if self.task_status:
            return
        self.toggleTaskStatusSignal.emit(True)

        # 处理数据
        message_info = self.process_message_info(message_info=message_info)
        runnable = TaskRunnable(
            self.wx.send_msg,
            message_info=message_info,
            check_pause=check_pause,
            updatedProgressSignal=updatedProgressSignal,
            toggleTaskStatusSignal=self.toggleTaskStatusSignal,
            recordExecInfoSignal=self.recordExecInfoSignal,
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
    def change_task_status(self, task_status_flag):
        # print('changed task status =>', task_status_flag, not task_status_flag)
        self.task_status = not self.task_status

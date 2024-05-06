# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2022-09-11 17:16
# @Name   : wx_operation.py

"""微信群发消息"""

import time
from copy import deepcopy
from typing import Iterable

import uiautomation as auto

from config import AutomationConfig as Config
from utils import (copy_files_to_clipboard, minimize_wechat, wake_up_window)


def set_default_timeout(seconds: float = 0.0):
    if seconds:
        auto.SetGlobalSearchTimeout(seconds)
    else:
        auto.SetGlobalSearchTimeout(3)


class WxOperation:
    """
    微信群发消息的类，提供了与微信应用交互的方法集，用于发送消息，管理联系人列表等功能。

    Attributes:
    ----------
    wx_window: auto.WindowControl
        微信控制窗口
    input_edit: wx_window.EditControl
        聊天界面输入框编辑控制窗口

    Methods:
    -------
    __goto_chat_box(name):
        跳转到 指定好友窗口
    __send_text(*msgs):
        发送文本。
    __send_file(*filepath):
        发送文件
    get_friend_list(tag, num):
        可指定tag，获取好友num页的好友数量
    send_msg(name, msgs, file_paths=None, add_remark_name=False, at_everyone=False,
            text_interval=0.05, file_interval=0.5) -> None:
        向指定的好友或群聊发送消息和文件。支持同时发送文本和文件。
    """

    def __init__(self):
        set_default_timeout(0.1)
        # Windows系统层面唤醒微信窗口
        wake_up_window(class_name=Config.WECHAT_WINDOW_CLASSNAME, name=Config.WECHAT_WINDOW_NAME)
        self.wx_window = auto.WindowControl(Name=Config.WECHAT_WINDOW_NAME, ClassName=Config.WECHAT_WINDOW_CLASSNAME)
        # assert self.wx_window.Exists(1.5, .5), "窗口不存在"
        if not self.wx_window.Exists(1, .5):
            raise Exception('微信似乎并没有登录!')
        self.input_edit = self.wx_window.EditControl()

    def __del__(self):
        minimize_wechat(class_name=Config.WECHAT_WINDOW_CLASSNAME, name=Config.WECHAT_WINDOW_NAME)

    def __match_nickname(self, name) -> bool:
        """获取当前面板的好友昵称"""
        self.input_edit = self.wx_window.EditControl(Name=name)
        if self.input_edit.Exists(0.1, 0.05):
            return True
        return False

    def __goto_chat_box(self, name: str) -> bool:
        """
        跳转到指定 name好友的聊天窗口。

        Args:
            name(str): 必选参数，好友名称

        Returns:
            None
        """
        assert name, "无法跳转到名字为空的聊天窗口"
        self.wx_window.SendKeys(text='{Ctrl}f', waitTime=0.2)
        self.wx_window.SendKeys(text='{Ctrl}a', waitTime=0.1)
        self.wx_window.SendKey(key=auto.SpecialKeyNames['DELETE'])
        auto.SetClipboardText(text=name)
        time.sleep(.2)
        self.wx_window.SendKeys(text='{Ctrl}v', waitTime=0.1)
        for idx, item in enumerate(self.wx_window.ListControl(foundIndex=2).GetChildren()):
            _name = item.Name
            if idx == 0:  # 跳过第一个 标签
                continue
            if _name == "":
                self.wx_window.SendKeys(text='{Esc}', waitTime=0.1)  # 没有匹配的用户, 取消搜索
                return False
            if _name == name:
                self.wx_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=0.2)
                time.sleep(.2)
                return True
        return False

    def at_at_everyone(self, group_chat_name: str):
        """
        @全部人的操作
        Args:
            group_chat_name(str): 群聊名称

        """
        # 个人 定位 聊天框，取 foundIndex=2，因为左侧聊天List 也可以匹配到foundIndex=1
        # 群聊 定位 聊天框 需要带上群人数，故会匹配失败，所以匹配失败的就是群聊
        result = self.wx_window.TextControl(Name=group_chat_name, foundIndex=2)
        # 只要匹配不上，说明这是个群聊窗口
        if not result.Exists(maxSearchSeconds=0.2, searchIntervalSeconds=0.1):
            # 寻找是否有 @所有人 的选项
            self.input_edit.SendKeys(text='{Shift}2', waitTime=0.1)
            everyone = self.wx_window.ListItemControl(Name='所有人')
            if not everyone.Exists(maxSearchSeconds=0.2, searchIntervalSeconds=0.1):
                self.input_edit.SendKeys(text='{Ctrl}A', waitTime=0.1)
                self.input_edit.SendKeys(text='{Delete}', waitTime=0.1)
                return
            self.input_edit.SendKeys(text='{Up}', waitTime=0.1)
            self.input_edit.SendKeys(text='{Enter}', waitTime=0.1)
            self.input_edit.SendKeys(text='{Enter}', waitTime=0.1)

    def __send_text(self, *msgs, wait_time=0.05) -> None:
        """
        发送文本.

        Args:
            input_name(str): 必选参数, 为输入框
            *msgs(str): 必选参数，为发送的文本
            wait_time(float): 可选参数，为动态等待时间，默认为0.02秒

        Returns:
            None
        """

        def should_use_clipboard(text: str):
            # 简单的策略：如果文本过长或包含特殊字符，则使用剪贴板
            return len(text) > 30 or not text.isprintable()

        for msg in msgs:
            assert msg, "发送的文本内容为空"
            self.input_edit.SendKeys(text='{Ctrl}a', waitTime=wait_time)
            self.input_edit.SendKey(key=auto.SpecialKeyNames['DELETE'], waitTime=wait_time)
            self.input_edit.SendKeys(text='{Ctrl}a', waitTime=wait_time)
            self.input_edit.SendKey(key=auto.SpecialKeyNames['DELETE'], waitTime=wait_time)

            if should_use_clipboard(msg):
                auto.SetClipboardText(text=msg)
                time.sleep(wait_time * 2.5)
                self.input_edit.SendKeys(text='{Ctrl}v', waitTime=wait_time * 2)
            else:
                self.input_edit.SendKeys(text=msg, waitTime=wait_time * 2)

            # 设置到剪切板再黏贴到输入框
            self.wx_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=wait_time * 2)

    def __send_file(self, *file_paths, wait_time=0.5) -> None:
        """
        发送文件.

        Args:
            *file_paths(str): 必选参数，为文件的路径

        Returns:
            None
        """
        # 复制文件到剪切板
        copy_files_to_clipboard(file_paths=file_paths)
        # 粘贴
        self.input_edit.SendKeys(text='{Ctrl}V', waitTime=wait_time)
        # 按下回车键
        self.wx_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=wait_time)
        time.sleep(wait_time)  # 等待发送动作完成

    def get_friend_list(self, tag: str = None, num: int = 10) -> list:
        """
        获取微信好友名称.

        Args:
            tag(str): 可选参数，如不指定，则获取所有好友
            num(int): 可选参数，如不指定，只获取10页好友

        Returns:
            list
        """

        def click_tag():
            """点击标签"""
            contacts_management_window.ButtonControl(Name="标签").Click()

        # 点击 通讯录管理
        self.wx_window.ButtonControl(Name="通讯录").Click()
        self.wx_window.ListControl(Name="联系人").ButtonControl(Name="通讯录管理").Click()
        contacts_management_window = auto.GetForegroundControl()  # 切换到通讯录管理，相当于切换到弹出来的页面
        # contacts_management_window.ButtonControl(Name='最大化').Click()

        if tag:
            click_tag()  # 点击标签
            contacts_management_window.PaneControl(Name=tag).Click()
            time.sleep(0.3)
            click_tag()  # 关闭标签
        # 获取滑动模式
        scroll = contacts_management_window.ListControl().GetScrollPattern()
        name_list = list()
        if not scroll:
            for name_node in contacts_management_window.ListControl().GetChildren():  # 获取当前页面的 列表 -> 子节点
                nick_name = name_node.TextControl().Name  # 用户名
                remark_name = name_node.ButtonControl(foundIndex=2).Name  # 用户备注名，索引1会错位，索引2是备注名，索引3是标签名
                name_list.append(remark_name if remark_name else nick_name)
        else:
            rate: int = int(float(102000 / num))  # 根据输入的num计算滑动的步长
            for pct in range(0, 102000, rate):  # range不支持float，不导入numpy库，采取迂回这的方式
                # 每次滑动一点点，-1代表不用滑动
                scroll.SetScrollPercent(horizontalPercent=-1, verticalPercent=pct / 100000)
                for name_node in contacts_management_window.ListControl().GetChildren():  # 获取当前页面的 列表 -> 子节点
                    nick_name = name_node.TextControl().Name  # 用户名
                    remark_name = name_node.ButtonControl(foundIndex=2).Name  # 用户备注名，索引1会错位，索引2是备注名，索引3是标签名
                    name_list.append(remark_name if remark_name else nick_name)
        contacts_management_window.SendKey(auto.SpecialKeyNames['ESC'])  # 结束时候关闭 "通讯录管理" 窗口
        return list(set(name_list))  # 简单去重，但是存在误判（如果存在同名的好友

    def get_group_chat_list(self) -> list:
        """获取群聊通讯录中的用户名称"""
        name_list = list()
        auto.ButtonControl(Name='聊天信息').Click()
        time.sleep(0.5)
        chat_members_win = self.wx_window.ListControl(Name='聊天成员')
        if not chat_members_win.Exists():
            return list()
        self.wx_window.ButtonControl(Name='查看更多').Click()
        for item in chat_members_win.GetChildren():
            name_list.append(item.ButtonControl().Name)
        return name_list

    def send_msg(self, name, msgs=None, file_paths=None,
                 add_remark_name=False, at_everyone=False, text_interval=0.05, file_interval=0.5) -> None:
        """
        发送消息，可同时发送文本和文件（至少选一项

        Args:
            name(str):必选参数，接收消息的好友名称, 可以单发
            msgs(Iterable[str], Optional): 可选参数，发送的文本消息
            file_paths(Iterable[str], Optional):可选参数，发送的文件路径
            add_remark_name(bool): 可选参数，是否添加备注名称发送
            at_everyone(bool): 可选参数，是否@全部人
            text_interval(float): 可选参数，默认为0.05
            file_interval(float): 可选参数，默认为0.5

        Raises:
            ValueError: 如果用户名为空或发送的消息和文件同时为空时抛出异常
            TypeError: 如果发送的文本消息或文件路径类型不是列表或元组时抛出异常
        """
        if not name:
            raise ValueError("用户名不能为空")

        if not any([msgs, file_paths]):
            raise ValueError("发送的消息和文件不可同时为空")

        if msgs and not isinstance(msgs, Iterable):
            raise TypeError("发送的文本消息必须是可迭代的")

        if file_paths and not isinstance(file_paths, Iterable):
            raise TypeError("发送的文件路径必须是可迭代的")

        # 如果当前面板已经是需发送好友, 则无需再次搜索跳转
        if not self.__match_nickname(name=name):
            if not self.__goto_chat_box(name=name):
                raise NameError('昵称不匹配')

        # 设置输入框为当前焦点
        self.input_edit = self.wx_window.EditControl(Name=name)
        self.input_edit.SetFocus()

        # @所有人
        if at_everyone:
            set_default_timeout(0.2)
            self.at_at_everyone(group_chat_name=name)
            set_default_timeout()

        # TODO
        #  添加备注可以多做一个选项，添加到每条消息的前面，如xxx，早上好
        if msgs and add_remark_name:
            new_msgs = deepcopy(list(msgs))
            new_msgs.insert(0, name)
            self.__send_text(*new_msgs, wait_time=text_interval)
        elif msgs:
            self.__send_text(*msgs, wait_time=text_interval)
        if file_paths:
            self.__send_file(*file_paths, wait_time=file_interval)
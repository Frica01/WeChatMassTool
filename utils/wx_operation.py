# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2022-09-11 17:16
# @Name   : wx_operation.py

"""微信群发消息"""

import time
from copy import deepcopy
from typing import Iterable

import uiautomation as auto

from config import (WeChat, Interval)
from utils import (copy_files_to_clipboard, wake_up_window, is_window_visible)


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
        self.wx_window = None
        self.input_edit = None
        self.wx_window: auto.WindowControl
        self.input_edit: auto.EditControl
        auto.SetGlobalSearchTimeout(Interval.BASE_INTERVAL)
        self.visible_flag: bool = False

    def locate_wechat_window(self):
        if not self.visible_flag:
            wake_up_window(class_name=WeChat.WINDOW_CLASSNAME, name=WeChat.WINDOW_NAME)
            self.wx_window = auto.WindowControl(Name=WeChat.WINDOW_NAME, ClassName=WeChat.WINDOW_CLASSNAME)
            if not self.wx_window.Exists(Interval.MAX_SEARCH_SECOND, searchIntervalSeconds=Interval.MAX_SEARCH_INTERVAL):
                raise Exception('微信似乎并没有登录!')
            self.input_edit = self.wx_window.EditControl()
            self.visible_flag = bool(self.visible_flag)
        # 微信窗口置顶
        self.wx_window.SetTopmost(isTopmost=True)

    def __match_nickname(self, name) -> bool:
        """获取当前面板的好友昵称"""
        self.input_edit = self.wx_window.EditControl(Name=name)
        if self.input_edit.Exists(Interval.MAX_SEARCH_SECOND, searchIntervalSeconds=Interval.MAX_SEARCH_INTERVAL):
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
        self.wx_window.SendKeys(text='{Ctrl}F', waitTime=Interval.BASE_INTERVAL)
        self.wx_window.SendKeys(text='{Ctrl}A', waitTime=Interval.BASE_INTERVAL)
        self.wx_window.SendKey(key=auto.SpecialKeyNames['DELETE'])
        auto.SetClipboardText(text=name)
        time.sleep(Interval.BASE_INTERVAL)
        self.wx_window.SendKeys(text='{Ctrl}V', waitTime=Interval.BASE_INTERVAL)
        # 若有匹配结果，第一个元素的类型为PaneControl
        search_nodes = self.wx_window.ListControl(foundIndex=2).GetChildren()
        if not isinstance(search_nodes.pop(0), auto.PaneControl):
            self.wx_window.SendKeys(text='{Esc}', waitTime=Interval.BASE_INTERVAL)
            raise ValueError("昵称不匹配")
        # 只考虑全匹配, 不考虑好友昵称重名, 不考虑好友昵称与群聊重名
        if search_nodes[0].Name == name:
            self.wx_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=Interval.BASE_INTERVAL)
            time.sleep(Interval.BASE_INTERVAL)
            return True
        # 无匹配用户, 取消搜索框
        self.wx_window.SendKeys(text='{Esc}', waitTime=Interval.BASE_INTERVAL)
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
        if not result.Exists(Interval.MAX_SEARCH_SECOND, searchIntervalSeconds=Interval.MAX_SEARCH_INTERVAL):
            # 寻找是否有 @所有人 的选项
            self.input_edit.SendKeys(text='{Shift}2', waitTime=Interval.BASE_INTERVAL)
            everyone = self.wx_window.ListItemControl(Name='所有人')
            if not everyone.Exists(Interval.MAX_SEARCH_SECOND, searchIntervalSeconds=Interval.MAX_SEARCH_INTERVAL):
                self.input_edit.SendKeys(text='{Ctrl}A', waitTime=Interval.BASE_INTERVAL)
                self.input_edit.SendKeys(text='{Delete}', waitTime=Interval.BASE_INTERVAL)
                return
            self.input_edit.SendKeys(text='{Up}', waitTime=Interval.BASE_INTERVAL)
            self.input_edit.SendKeys(text='{Enter}', waitTime=Interval.BASE_INTERVAL)
            self.input_edit.SendKeys(text='{Enter}', waitTime=Interval.BASE_INTERVAL)

    def __send_text(self, *msgs, wait_time, send_shortcut) -> None:
        """
        发送文本.

        Args:
            input_name(str): 必选参数, 为输入框
            *msgs(str): 必选参数，为发送的文本
            wait_time(float): 必选参数，为动态等待时间
            send_shortcut(str): 必选参数，为发送快捷键

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
            self.wx_window.SendKeys(text=f'{send_shortcut}', waitTime=wait_time * 2)

    def __send_file(self, *file_paths, wait_time, send_shortcut) -> None:
        """
        发送文件.

        Args:
            *file_paths(str): 必选参数，为文件的路径
            wait_time(float): 必选参数，为动态等待时间
            send_shortcut(str): 必选参数，为发送快捷键

        Returns:
            None
        """
        # 复制文件到剪切板
        if copy_files_to_clipboard(file_paths=file_paths):
            # 粘贴到输入框
            self.input_edit.SendKeys(text='{Ctrl}V', waitTime=wait_time)
            # 按下回车键
            self.wx_window.SendKeys(text=f'{send_shortcut}', waitTime=wait_time / 2)

            time.sleep(wait_time)  # 等待发送动作完成

    def get_friend_list(self, tag: str = None) -> list:
        """
        获取微信好友名称.

        Args:
            tag(str): 可选参数，如不指定，则获取所有好友

        Returns:
            list
        """
        # 定位到微信窗口
        self.locate_wechat_window()
        # 取消微信窗口置顶
        self.wx_window.SetTopmost(isTopmost=False)
        # 点击 通讯录管理
        self.wx_window.ButtonControl(Name="通讯录").Click(simulateMove=False)
        self.wx_window.ListControl(Name="联系人").ButtonControl(Name="通讯录管理").Click(simulateMove=False)
        # 切换到通讯录管理，相当于切换到弹出来的页面
        contacts_window = auto.GetForegroundControl()
        contacts_window.ButtonControl(Name='最大化').Click(simulateMove=False)

        if tag:
            try:
                contacts_window.ButtonControl(Name="标签").Click(simulateMove=False)
                contacts_window.PaneControl(Name=tag).Click(simulateMove=False)
                time.sleep(Interval.BASE_INTERVAL * 2)
            except LookupError:
                contacts_window.SendKey(auto.SpecialKeyNames['ESC'])
                raise LookupError(f'找不到 {tag} 标签')

        name_list = list()
        last_names = None
        while True:
            # TODO 修改成使用 foundIndex 的方式
            try:
                nodes = contacts_window.ListControl(foundIndex=2).GetChildren()
            except LookupError:
                nodes = contacts_window.ListControl().GetChildren()
            cur_names = [node.TextControl().Name for node in nodes]

            # 如果滚动前后名单未变，认为到达底部
            if cur_names == last_names:
                break
            last_names = cur_names
            # 处理当前页的名单
            for node in nodes:
                # TODO 如果有需要, 可以处理成导出为两列的csv格式
                nick_name = node.TextControl().Name  # 用户名
                remark_name = node.ButtonControl(foundIndex=2).Name  # 用户备注名，索引1会错位，索引2是备注名，索引3是标签名
                name_list.append(remark_name if remark_name else nick_name)
            # 向下滚动页面
            contacts_window.WheelDown(wheelTimes=8, waitTime=Interval.BASE_INTERVAL / 2)
        # 结束时候关闭 "通讯录管理" 窗口
        contacts_window.SendKey(auto.SpecialKeyNames['ESC'])
        # 简单去重，但是存在误判（如果存在同名的好友), 保持获取时候的顺序
        return list(dict.fromkeys(name_list))

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

    def send_msg(self, name, msgs=None, file_paths=None, add_remark_name=False, at_everyone=False,
                 text_interval=Interval.SEND_TEXT_INTERVAL, file_interval=Interval.SEND_FILE_INTERVAL,
                 send_shortcut='{Enter}') -> None:
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
            send_shortcut(str): 可选参数，默认为 Enter

        Raises:
            ValueError: 如果用户名为空或发送的消息和文件同时为空时抛出异常
            TypeError: 如果发送的文本消息或文件路径类型不是列表或元组时抛出异常
        """

        # 定位到微信窗口
        self.locate_wechat_window()

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
            auto.SetGlobalSearchTimeout(Interval.BASE_INTERVAL)
            self.at_at_everyone(group_chat_name=name)
            auto.SetGlobalSearchTimeout(Interval.BASE_INTERVAL * 25)

        # TODO
        #  添加备注可以多做一个选项，添加到每条消息的前面，如xxx，早上好
        if msgs and add_remark_name:
            new_msgs = deepcopy(list(msgs))
            new_msgs.insert(0, name)
            self.__send_text(*new_msgs, wait_time=text_interval, send_shortcut=send_shortcut)
        elif msgs:
            self.__send_text(*msgs, wait_time=text_interval, send_shortcut=send_shortcut)
        if file_paths:
            self.__send_file(*file_paths, wait_time=file_interval, send_shortcut=send_shortcut)

        # 取消微信窗口置顶
        self.wx_window.SetTopmost(isTopmost=False)


if __name__ == '__main__':
    wx = WxOperation()
    data = wx.get_friend_list('无标签')
    print(data)
    print(data.__len__())

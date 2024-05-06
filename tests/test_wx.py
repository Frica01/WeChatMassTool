# -*- coding: utf-8 -*-
# Name:         test_wx.py
# Author:       小菜
# Date:         2024/4/1 00:00
# Description:

from utils import WxOperation

wx = WxOperation()

wx.send_msg('小菜',
            [1123],
            add_remark_name=True
            )



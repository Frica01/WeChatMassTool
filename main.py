# -*- coding: utf-8 -*-
# Name:         main.py
# Author:       小菜
# Date:         2024/4/01 00:00
# Description:

import datetime
import platform
import sys
from ctypes import windll

import PySide6
import uiautomation
from PySide6 import QtGui
from PySide6.QtWidgets import (QApplication, QMessageBox, QWidget)
from cprint import cprint

from config import (Animate, WeChat)
from controllers import ControllerMain
from utils import (
    get_specific_process, is_process_running, get_resource_path, get_config, minimize_wechat, write_file, delete_file,
    path_exists, get_temp_file_path, read_file, get_pid, delete_old_files_with_extension, join_path
)
from version import (__version__, __project_name__, __author__)


def set_app_user_model_id() -> None:
    """设置应用程序用户模型ID"""
    try:
        myapp_id = 'myapp_id'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
    except (ImportError, AttributeError, OSError):
        # 兼容非Windows系统或缺少相关库的情况
        pass


def print_startup_info() -> None:
    """打印程序启动信息"""
    # 获取系统信息
    system_info = platform.uname()

    bot_logo = r""" 

    /¯¯¯¯\         /¯¯¯¯\         /¯¯¯¯\     
  o-|[][]|-o     o-|[][]|-o     o-|[][]|-o   
    |_--_|         |_--_|         |_--_|     
 /¯¯¯¯¯¯¯¯¯¯\   /¯¯¯¯¯¯¯¯¯¯\   /¯¯¯¯¯¯¯¯¯¯\  
 |||  «»  |||   |||  «»  |||   |||  «»  |||  
 |||      |||   |||      |||   |||      |||  
(o)|      |(o) (o)|      |(o) (o)|      |(o) 
   |  ||  |       |  ||  |       |  ||  |    
   |__||__|       |__||__|       |__||__|    
   |__||__|       |__||__|       |__||__|
"""
    # 启动信息
    startup_info = f"""
        项目名称: {__project_name__}
        版本: {__version__}
        作者: {__author__}
        启动时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        系统: {system_info.system} {system_info.release}
        版本: {system_info.version}
        处理器: {system_info.processor}
        Python: {platform.python_version()}
        PySide6: {PySide6.__version__}
        uiautomation: {uiautomation.version.VERSION}

        项目启动中...
    """
    cprint.info(bot_logo.rstrip('\n'))
    cprint.info(startup_info.rstrip('\n'))


def check_wechat_running() -> None:
    """检查微信是否运行"""
    if not get_specific_process(proc_name=WeChat.WeChat_PROCESS_NAME):
        QMessageBox.critical(QWidget(), '报错咯', "微信未启动!")
        sys.exit(1)  # 使用非零退出码表示异常退出


def initialize_application() -> None:
    """初始化应用程序"""
    app = QApplication()
    app.setWindowIcon(QtGui.QIcon(get_resource_path(r'views/resources/images/favicon.ico')))
    check_wechat_running()
    
    # 获取默认配置, 看是否需要以动画形式启动
    animate_startup = get_config(WeChat.APP_NAME, section=Animate.SECTION, option=Animate.OPTION)
    controller = ControllerMain(animate_startup)
    
    # 绑定退出事件, 关闭微信窗口
    app.aboutToQuit.connect(
        lambda: minimize_wechat(WeChat.WINDOW_CLASSNAME, name=WeChat.WINDOW_NAME)
    )
    sys.exit(app.exec())


def ensure_single_instance() -> None:
    """用于保证只能有一个应用程序实例运行"""
    # 使用文件锁来保证单实例运行, 获取系统存储临时文件路径
    lock_file = get_temp_file_path(file_name=join_path(WeChat.APP_NAME, WeChat.APP_LOCK_NAME))

    # 检查并删除过时的锁文件
    if path_exists(lock_file):
        try:
            # 检查是否有进程在运行
            lock_content = read_file(lock_file)
            if lock_content and not is_process_running(
                pid=int(lock_content[0]), proc_name=WeChat.APP_PROCESS_NAME
            ):
                delete_file(lock_file)
        except (FileExistsError, FileNotFoundError, ValueError, IndexError):
            # 锁文件损坏或无法读取，直接删除
            delete_file(lock_file)

    if path_exists(lock_file):
        print("另一个实例已经在运行。")
        sys.exit(1)

    # 创建锁文件
    write_file(lock_file, data=[str(get_pid())])


def main() -> None:
    """主入口"""
    try:
        # 删除三天前的进度缓存文件
        delete_old_files_with_extension(get_temp_file_path(WeChat.APP_NAME), days=3, file_extension='.tmp')
        # 删除运行缓存文件
        delete_old_files_with_extension(
            get_temp_file_path(join_path(WeChat.APP_NAME, '.cache')), days=0, file_extension='.pkl'
        )

        # 保证只有一个应用实例运行
        ensure_single_instance()

        # 正常走的流程
        set_app_user_model_id()
        print_startup_info()  # 打印启动信息
        initialize_application()
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
        sys.exit(0)
    except Exception as e:
        print(f"程序启动时发生未预期的错误: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

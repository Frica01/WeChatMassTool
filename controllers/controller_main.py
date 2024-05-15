# -*- coding: utf-8 -*-
# Name:         controller_main.py
# Author:       小菜
# Date:         2024/04/01 00:00
# Description:


from PySide6.QtCore import (QObject, QMutexLocker, QMutex, QWaitCondition)
from PySide6.QtWidgets import (QFileDialog, QMessageBox)

from models import ModelMain
from utils import (read_file, write_config)
from config import (Animate, WeChat)
from views import ViewMain


class ControllerMain(QObject):

    def __init__(self, animate_on_startup=True, parent=None):
        super().__init__(parent)
        self.view = ViewMain(animate_on_startup)
        self.model = ModelMain()

        # 互斥锁 和 条件等待
        self.paused = False
        self.mutex = QMutex()
        self.pause_condition = QWaitCondition()
        #
        self.setup_connections()
        self.name_list = list()
        self.init_animate_radio_btn(flag=animate_on_startup)

    def setup_connections(self):
        # 发送消息
        self.view.btn_send_msg.clicked.connect(self.on_send_clicked)
        self.view.btn_pause_send.clicked.connect(self.toggle_send_status)
        # 清空控件
        self.view.btn_clear_msg.clicked.connect(self.view.clear_msg_text_edit)
        self.view.btn_clear_name.clicked.connect(self.clear_name_actions)
        self.view.btn_clear_file.clicked.connect(self.view.clear_file_list_widget)
        self.view.btn_clear_all.clicked.connect(self.clear_all_actions)
        # 添加文件
        self.view.btn_add_file.clicked.connect(self.import_send_file)
        self.view.filesDropped.connect(self.import_send_file)
        self.view.btn_import_name_list.clicked.connect(self.import_name_list_file)
        self.view.btn_export_name_list.clicked.connect(self.export_tag_name_list)
        # 导出运行结果
        self.view.btn_export_result.clicked.connect(self.export_exec_result)
        # 添加 QListWidget 控件右键菜单
        self.view.add_list_widget_menu()
        #
        self.view.updatedProgressSignal.connect(self.view.update_progress)
        self.model.exportNameListSignal.connect(self.show_export_msg_box)

        #
        self.view.radio_btn_animate_true.clicked.connect(self.set_animate_startup_status)
        self.view.radio_btn_animate_false.clicked.connect(self.set_animate_startup_status)

    def get_gui_info(self):
        single_text = self.view.single_line_msg_text_edit.toPlainText()
        multi_text = self.view.multi_line_msg_text_edit.toPlainText()
        files = [self.view.file_list_widget.item(row).text() for row in range(self.view.file_list_widget.count())]
        names = self.view.name_text_edit.toPlainText()
        add_remark_name = True if self.view.rb_add_remark.isChecked() else False
        at_everyone = True if self.view.rb_at_everyone.isChecked() else False
        text_interval = float(self.view.cb_text_interval.currentText())
        file_interval = float(self.view.cb_file_interval.currentText())
        return {
            'single_text': single_text,
            'multi_text': multi_text,
            'file_paths': files,
            'names': names,
            'name_list': self.name_list,
            'add_remark_name': add_remark_name,
            'at_everyone': at_everyone,
            'text_interval': text_interval,
            'file_interval': file_interval,
        }

    # noinspection PyUnresolvedReferences
    def import_name_list_file(self) -> None:
        """添加昵称清单"""
        if name_list_file := QFileDialog.getOpenFileName(self.view, '选择文件', '', "Text Files (*.txt)")[0]:
            self.view.set_text_in_widget('import_name_list_line_edit', name_list_file)
            self.name_list = read_file(file=name_list_file)
            self.view.show_message_box('导入成功!', QMessageBox.Information)
        else:
            self.name_list = list()
            self.view.set_text_in_widget('import_name_list_line_edit', '')
            self.view.show_message_box('导入失败!', QMessageBox.Critical, duration=3000)

    def import_send_file(self, new_files):
        if not new_files:
            new_files = set(QFileDialog.getOpenFileNames(self.view, '选择文件', "All Files (*);;*")[0])
        curr_files = {self.view.file_list_widget.item(row).text() for row in range(self.view.file_list_widget.count())}
        # 计算尚未添加到列表的新文件
        if files_to_add := (new_files - curr_files):
            self.view.file_list_widget.addItems(files_to_add)

    def export_tag_name_list(self):
        if not self.view.export_tag_name_list_line_edit.text():
            self.view.show_message_box('无标签名称!', QMessageBox.Critical, duration=1500)
            return
        if file_path := QFileDialog.getSaveFileName(self.view, "Create File", "untitled.txt", "Text Files (*.txt)")[0]:
            if file_path.endswith('.txt'):
                # 保存文件
                self.model.get_name_list(self.view.export_tag_name_list_line_edit.text(), file_path)
        else:
            self.name_list = list()
            self.view.set_text_in_widget('export_tag_name_list_line_edit', '')
            self.view.show_message_box('导入失败!', QMessageBox.Critical, duration=3000)
            return

    def on_send_clicked(self):
        data = self.get_gui_info()
        print(data)
        self.model.send_wechat_message(
            data,
            check_pause=self.check_pause,
            updatedProgressSignal=self.view.updatedProgressSignal,
        )

    def check_pause(self):
        """检查暂停"""
        if self.paused:
            with QMutexLocker(self.mutex):
                self.pause_condition.wait(self.mutex)

    def toggle_send_status(self):
        """切换暂停状态"""
        self.paused = not self.paused
        with QMutexLocker(self.mutex):
            if not self.paused:
                self.pause_condition.wakeAll()
        # 切换按钮文本 和 图标
        current_text = self.view.btn_pause_send.text()
        self.view.btn_pause_send.setText('暂停发送' if current_text == '继续发送' else '继续发送')
        self.view.pause_and_continue_send()

    # noinspection PyUnresolvedReferences
    def export_exec_result(self):
        """导出运行结果"""
        if self.model.record.export_exec_result_to_csv('运行结果.csv'):
            self.view.show_message_box('导出成功!', QMessageBox.Information)
        else:
            self.view.show_message_box('导出失败!', QMessageBox.Critical, duration=3000)

    def clear_name_actions(self):
        """清空 名字清单 控件"""
        self.view.clear_name_text_edit()
        self.name_list = list()

    def clear_all_actions(self):
        """清空 全部 控件"""
        self.view.clear_all_text_edit()
        self.name_list = list()

    def init_animate_radio_btn(self, flag):
        if flag:
            self.view.radio_btn_animate_true.click()
        else:
            self.view.radio_btn_animate_false.click()

    def set_animate_startup_status(self):
        if self.view.radio_btn_animate_true.isChecked():
            write_config(WeChat.APP_NAME, Animate.SECTION, Animate.OPTION, value=str(True))
        else:
            write_config(WeChat.APP_NAME, Animate.SECTION, Animate.OPTION, value=str(False))

    def show_export_msg_box(self, status, tip):
        icon = QMessageBox.Information if status else QMessageBox.Critical
        self.view.show_message_box(message=tip, icon=icon)

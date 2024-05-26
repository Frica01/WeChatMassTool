# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024-04-12 0:23
# @Name   : model_generator_csv.py


import pickle
import os
import csv

from config import WeChat
from utils import (get_temp_file_path, join_path)


class RecordGeneratorModel:
    def __init__(self):
        self.cache_dir = get_temp_file_path(join_path(WeChat.APP_NAME, '.cache'))
        self.temp_file_path = join_path(self.cache_dir, "exec_results.pkl")
        os.makedirs(self.cache_dir, exist_ok=True)

    def record_exec_result(self, result):
        """记录执行结果"""
        with open(self.temp_file_path, 'ab') as file:
            pickle.dump(result, file)

    def load_exec_results(self):
        """加载执行结果"""
        results = []
        if os.path.exists(self.temp_file_path):
            with open(self.temp_file_path, 'rb') as file:
                while True:
                    try:
                        results.append(pickle.load(file))
                    except EOFError:
                        break
        return results

    def export_exec_result_to_csv(self, csv_filepath):
        """导出执行结果"""
        try:
            if results := self.load_exec_results():
                with open(csv_filepath, 'w', newline='') as csvfile:
                    # 定义CSV文件的列标题
                    fieldnames = ['昵称', '文本', '文件', '状态', '备注']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for result in results:
                        writer.writerow(result)
                return {'status': True, 'tip': '导出成功!'}
            return {'status': False, 'tip': '运行结果为空!'}
        except Exception as e:
            return {'status': False, 'tip': str(e)}

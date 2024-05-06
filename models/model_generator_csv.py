# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024-04-12 0:23
# @Name   : model_generator_csv.py


import pickle
import os
import csv


class RecordGeneratorModel:
    def __init__(self):
        self.cache_dir = "./.cache"
        self.temp_file_path = os.path.join(self.cache_dir, "exec_results.pkl")
        os.makedirs(self.cache_dir, exist_ok=True)

    def record_exec_result(self, result):
        # result应为字典格式，如{'发送文本': 'xxx', '发送文件': 'xxx', '状态': 'xxx'}
        with open(self.temp_file_path, 'ab') as file:
            pickle.dump(result, file)

    def load_exec_results(self):
        results = []
        if os.path.exists(self.temp_file_path):
            with open(self.temp_file_path, 'rb') as file:
                while True:
                    try:
                        results.append(pickle.load(file))
                    except EOFError:
                        break
        return results

    def cleanup(self):
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)
        if os.path.exists(self.cache_dir):
            os.rmdir(self.cache_dir)

    def export_exec_result_to_csv(self, csv_filepath):
        try:
            results = self.load_exec_results()
            with open(csv_filepath, 'w', newline='') as csvfile:
                # 定义CSV文件的列标题
                fieldnames = ['昵称', '文本', '文件', '状态', '备注']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for result in results:
                    writer.writerow(result)
            return True
        except Exception as e:
            print(e)
            return False

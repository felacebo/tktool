"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
# 示例下载 https://www.pytk.net/blog/1702564569.html

import tkinter as tk
from tkinter import messagebox
import time

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
        self.ui.tk_text_ipTxt.insert(tk.END, "初始IP")
        self.ui.tk_text_pathTxt.insert(tk.END, "初始路径")
    def parseIp(self,evt):
        messagebox.showinfo('提示', message=self.ui.tk_text_ipTxt.get(1.0, "end-1c"))
    def start(self,evt):
        # messagebox.showinfo('提示', message=self.ui.tk_text_pathTxt.get(1.0, "end-1c"))
        for i in range(10):
            self.ui.tk_progressbar_progressBar['value'] += 10
            time.sleep(0.1)
            self.ui.update()
    def dSelete(self,evt):
        self.ui.tk_text_pathTxt.delete(1.0, "end")
        self.ui.tk_text_pathTxt.insert(tk.END, "Set D path")
    def pSelete(self,evt):
        self.ui.tk_text_pathTxt.delete(1.0, "end")
        self.ui.tk_text_pathTxt.insert(tk.END, "Set P path")
    def selfSelete(self,evt):
        self.ui.tk_text_pathTxt.delete(1.0, "end")
        self.ui.tk_text_pathTxt.insert(tk.END, "Set Self path")

"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.selected_value = IntVar()
        self.selected_value.set(1)
        self.tk_button_startButton = self.__tk_button_startButton(self)
        self.tk_text_ipTxt = self.__tk_text_ipTxt(self)
        self.tk_radio_button_dSelect = self.__tk_radio_button_dSelect(self)
        self.tk_radio_button_pSelect = self.__tk_radio_button_pSelect(self)
        self.tk_radio_button_selfSelect = self.__tk_radio_button_selfSelect(self)
        self.tk_text_pathTxt = self.__tk_text_pathTxt(self)
        self.tk_progressbar_progressBar = self.__tk_progressbar_progressBar(self)
        self.tk_button_parseIpButton = self.__tk_button_parseIpButton(self)
        self.tk_label_ipLabel = self.__tk_label_ipLabel(self)
        self.tk_label_path = self.__tk_label_path(self)
        self.tk_text_outputTxt = self.__tk_text_outputTxt(self)
        self.tk_label_outputLabel = self.__tk_label_outputLabel(self)
    def __win(self):
        self.title("TkTool")
        # 设置窗口大小、居中
        width = 500
        height = 440
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_button_startButton(self,parent):
        btn = Button(parent, text="开始", takefocus=False,)
        btn.place(x=21, y=300, width=50, height=30)
        return btn
    def __tk_text_ipTxt(self,parent):
        text = Text(parent)
        text.place(x=84, y=23, width=400, height=135)
        return text
    def __tk_radio_button_dSelect(self,parent):
        rb = Radiobutton(parent,text="D", variable=self.selected_value, value=1)
        rb.place(x=85, y=244, width=80, height=30)
        return rb
    def __tk_radio_button_pSelect(self,parent):
        rb = Radiobutton(parent,text="P", variable=self.selected_value, value=2)
        rb.place(x=183, y=244, width=80, height=30)
        return rb
    def __tk_radio_button_selfSelect(self,parent):
        rb = Radiobutton(parent,text="自定义", variable=self.selected_value, value=3)
        rb.place(x=282, y=244, width=80, height=30)
        return rb
    def __tk_text_pathTxt(self,parent):
        text = Text(parent)
        text.place(x=84, y=181, width=400, height=60)
        return text
    def __tk_progressbar_progressBar(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL, maximum=100)
        progressbar.place(x=84, y=299, width=400, height=30)
        return progressbar
    def __tk_button_parseIpButton(self,parent):
        btn = Button(parent, text="解析IP", takefocus=False,)
        btn.place(x=20, y=67, width=50, height=30)
        return btn
    def __tk_label_ipLabel(self,parent):
        label = Label(parent,text="IP",anchor="center", )
        label.place(x=20, y=24, width=50, height=30)
        return label
    def __tk_label_path(self,parent):
        label = Label(parent,text="路径",anchor="center", )
        label.place(x=20, y=182, width=50, height=30)
        return label
    def __tk_text_outputTxt(self,parent):
        text = Text(parent)
        text.place(x=84, y=340, width=400, height=80)
        return text
    def __tk_label_outputLabel(self,parent):
        label = Label(parent,text="输出",anchor="center", )
        label.place(x=20, y=342, width=50, height=30)
        return label
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_startButton.bind('<Button-1>',self.ctl.start)
        self.tk_button_parseIpButton.bind('<Button-1>',self.ctl.parseIp)
        self.tk_radio_button_dSelect.bind('<Button-1>',self.ctl.dSelete)
        self.tk_radio_button_pSelect.bind('<Button-1>',self.ctl.pSelete)
        self.tk_radio_button_selfSelect.bind('<Button-1>',self.ctl.selfSelete)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()

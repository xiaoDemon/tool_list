#!/usr/bin/python3

import tkinter
from tkinter import ttk
import xor_tk
import xml_parse
import version_tk

tool_window = 0
top_label = 0
frame_explain_label = 0
func_combobox_value_str = 0
func_combobox = 0
xor_frame = 0
xml_frame = 0
version_frame = 0


def frame_show_hide(number):
    if number == "1":
        xor_frame.pack()
        # xor_tk.new_window(tool_window)
    else:
        xor_frame.pack_forget()

    if number == "2":
        xml_frame.pack()
    else:
        xml_frame.pack_forget()

    if number == "3":
        version_frame.pack()
    else:
        version_frame.pack_forget()


def combobox_choose_func(*args):
    print(func_combobox.get())
    number = func_combobox.get()[:1]
    frame_show_hide(number)


def tk_label_init(tk_window):
    global top_label, frame_explain_label
    top_label = tkinter.Label(tk_window, text="工具选择", font=("宋体", 20))
    top_label.pack()


def tk_button_init(tk_window):
    pass


def tk_combobox_init(tk_window):
    global func_combobox_value_str, func_combobox
    func_combobox_value_str = tkinter.StringVar()
    func_combobox = ttk.Combobox(tk_window, width=50, textvariable=func_combobox_value_str, state="readonly")
    func_combobox['values'] = ("1、xor crc校验工具", "2、xml解析工具", "3、版本名字生成工具")
    func_combobox.current(0)
    func_combobox.bind("<<ComboboxSelected>>", combobox_choose_func)
    func_combobox.pack()


def tk_frame_init(tk_window):
    global xor_frame, xml_frame, version_frame
    xor_frame = tkinter.Frame(tk_window, width=700, height=480)
    xor_tk.init_param(xor_frame)
    xml_frame = tkinter.Frame(tk_window, width=700, height=480)
    xml_parse.init_ui(xml_frame)
    version_frame = tkinter.Frame(tk_window, width=700, height=480)
    version_tk.init_param(version_frame)


def tk_window_init(tk_window):
    tk_window.title("工具--V1.0")
    tk_window.geometry('800x600+10+10')
    tk_label_init(tk_window)
    tk_button_init(tk_window)
    tk_combobox_init(tk_window)
    tk_frame_init(tk_window)


if __name__ == "__main__":
    tool_window = tkinter.Tk()
    tk_window_init(tool_window)
    tool_window.mainloop()


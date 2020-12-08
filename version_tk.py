# FW_MPTL4.18_V04.01U_2019-09-09_STM32F107RCT6_1.HEX

# !/usr/bin/python3

import tkinter

init_data_text = 0
result_data_text = 0
type_data_text = 0
version_data_text = 0
date_data_text = 0
mcu_data_text = 0
pcb_data_text = 0
remark_data_text = 0


def func_xor_crc():
    global type_data_text, version_data_text, date_data_text, mcu_data_text, pcb_data_text, remark_data_text

    type_str = type_data_text.get(1.0, "end")
    version_str = version_data_text.get(1.0, "end")
    date_str = date_data_text.get(1.0, "end")
    mcu_str = mcu_data_text.get(1.0, "end")
    pcb_str = pcb_data_text.get(1.0, "end")
    remark_str = remark_data_text.get(1.0, "end")

    if remark_str[:-1] == "":
        result_str = "FW" + "_" + type_str[:-1] + "_" + version_str[:-1] + "_" + date_str[:-1] + "_" + \
                     mcu_str[:-1] + "_" + pcb_str[:-1]
    else:
        result_str = "FW"+"_"+type_str[:-1]+"_"+version_str[:-1]+"_"+date_str[:-1]+"_" + \
                    mcu_str[:-1]+"_"+pcb_str[:-1]+"_"+remark_str[:-1]

    result_data_text.delete(1.0, "end")
    result_data_text.insert(1.0, result_str)


def init_param(init_window_name):
    global type_data_text, version_data_text, date_data_text, mcu_data_text, pcb_data_text, \
        remark_data_text, result_data_text
    # 标签
    type_data_label = tkinter.Label(init_window_name, text="产品型号，不带hdl      (例子：MPTL4.18)")
    type_data_label.place(x=100, y=15)
    version_data_label = tkinter.Label(init_window_name, text="版本号     (例子：V04.01U)")
    version_data_label.place(x=100, y=75)
    date_data_label = tkinter.Label(init_window_name, text="日期      (例子：2019-09-09)")
    date_data_label.place(x=100, y=135)
    mcu_data_label = tkinter.Label(init_window_name, text="芯片型号     (例子：STM32F107RCT6)")
    mcu_data_label.place(x=100, y=195)
    pcb_data_label = tkinter.Label(init_window_name, text="硬件号      (例子：1)")
    pcb_data_label.place(x=100, y=255)
    remark_data_label = tkinter.Label(init_window_name, text="备注，可以为空")
    remark_data_label.place(x=100, y=315)
    result_data_label = tkinter.Label(init_window_name, text="输出结果")
    result_data_label.place(x=400, y=15)
    # 文本框
    type_data_text = tkinter.Text(init_window_name, width=30, height=2)
    type_data_text.place(x=100, y=40)
    version_data_text = tkinter.Text(init_window_name, width=30, height=2)
    version_data_text.place(x=100, y=100)
    date_data_text = tkinter.Text(init_window_name, width=30, height=2)
    date_data_text.place(x=100, y=160)
    mcu_data_text = tkinter.Text(init_window_name, width=30, height=2)
    mcu_data_text.place(x=100, y=220)
    pcb_data_text = tkinter.Text(init_window_name, width=30, height=2)
    pcb_data_text.place(x=100, y=280)
    remark_data_text = tkinter.Text(init_window_name, width=30, height=2)
    remark_data_text.place(x=100, y=340)
    result_data_text = tkinter.Text(init_window_name, width=50, height=10)  # 处理结果展示
    result_data_text.place(x=400, y=50)
    # 按键
    func_xor_button = tkinter.Button(init_window_name, text="生成", bg="white", width=10,
                                     command=func_xor_crc)
    func_xor_button.place(x=317, y=80)


def func_xor_crc_test():
    print("-" * 50)
    sum = 0
    input_str = input("请输入想异或的字符串\n"
                      "格式为0xXX 0xXX...\n")
    x = input_str.split()
    print(x)
    for i in x:
        i = int(i, 16)
        sum = sum ^ i
    print("异或结果为0x%x" % sum)
    print()


def new_window(window):
    init_window = tkinter.Toplevel(window)
    init_window.title("版本名字")
    init_window.geometry('800x480+10+10')
    init_param(init_window)


def gui_start():
    init_window = tkinter.Tk()
    init_window.title("版本名字")
    init_window.geometry('800x480+10+10')
    init_param(init_window)
    init_window.mainloop()


if __name__ == '__main__':
    gui_start()

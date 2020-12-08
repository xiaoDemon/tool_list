#!/usr/bin/python3
import tkinter

init_data_text = 0
result_data_text = 0


def func_xor_crc():
    sum = 0
    input_str = init_data_text.get(1.0, "end")
    x = input_str.split()
    print(x)
    for i in x:
        i = int(i, 16)
        sum = sum ^ i
    result_data_text.delete(1.0, "end")
    result_data_text.insert(1.0, "异或结果为" + "0x" + ("%x" % sum)[-2:])


def init_param(init_window_name):
    global init_data_text, result_data_text
    # 标签
    init_data_label = tkinter.Label(init_window_name, text="待处理数据:格式 0xXX 0xXX")
    init_data_label.place(x=100, y=15)
    result_data_label = tkinter.Label(init_window_name, text="输出结果")
    result_data_label.place(x=400, y=15)
    # 文本框
    init_data_text = tkinter.Text(init_window_name, width=30, height=10)
    init_data_text.place(x=100, y=50)
    result_data_text = tkinter.Text(init_window_name, width=30, height=10)  # 处理结果展示
    result_data_text.place(x=400, y=50)
    # 按键
    func_xor_button = tkinter.Button(init_window_name, text="计算", bg="white", width=10,
                                     command=func_xor_crc)
    func_xor_button.place(x=317, y=80)


def new_window(window):
    init_window = tkinter.Toplevel(window)
    init_window.title("xor-8位crc计算器")
    init_window.geometry('800x480+10+10')
    init_param(init_window)


def gui_start():
    init_window = tkinter.Tk()
    init_window.title("xor-8位crc计算器")
    init_window.geometry('800x480+10+10')
    init_param(init_window)
    init_window.mainloop()


if __name__ == '__main__':
    gui_start()

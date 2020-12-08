#!/usr/bin/python3
from xml.dom.minidom import parse
import tkinter
import tkinter.scrolledtext
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import tkinter.messagebox

xml_path = "E:/ctrlboard.xml"

type_list = ["AnalogClock", "Animation", "Audio", "Background", "BackgoundButton", "Blur", "Button", "Calendar",
             "CheckBox", " CircleProgressBar", "Clipper", "ColorPicker", "Container", "CoverFlow", "Curve",
             "DigitalClock", "DragIcon", "DrawPen", "FileListBox", "Icon", "IconListBox", "ImageCoverFlow",
             "Keyboard", "LanguageSprite", "ListBox", "MediaFileListBox", "Meter", "Oscilloscope", "PageFlow",
             "PopupButton", "PopupRadioBox", "ProgressBar", "RadioBox", "RippleBackground", "ScaleCoverFlow",
             "ScrollBar", "ScrollIconListBox", "ScrollListBox", "ScrollMediaFileListBox", "ScrollText",
             "Shadow", "SimpleAnimation", "Slideshow", "Sprite", "SpriteButton", "StepWheel", "StopAnyWhere",
             "TableIconListBox", "TableListBox", "Text", "TextBox", "TrackBar", "Video", "WaveBackground",
             "Wheel", "WheelBackground"]

# dom_tree = parse(xml_path)
# 文档根元素
# root_node = dom_tree.documentElement
# print(root_node.nodeName)

xml_path_text = 0
xml_result_text = 0
xml_func_combobox = 0

xml_input_frame = 0
input_str_frame = [1, 2, 3, 4, 5, 6, 7, 8]
input_str_text = [1, 2, 3, 4, 5, 6, 7, 8]
input_str_label = [1, 2, 3, 4, 5, 6, 7, 8]


def read_type_list():
    xml_result_text.insert("end", "***类型列表***" + '\n')
    for v in type_list:
        xml_result_text.insert("end", str(v) + '\n')
    xml_result_text.insert("end", "****************" + '\n')


def get_widget_type_str(widget):
    widget_type = widget.getAttribute("type")
    s_index = widget_type.find(".") + 1
    e_index = widget_type.find("Widget")
    return widget_type[s_index:e_index]


def readXML():
    widget_sum = 0
    widgets = root_node.getElementsByTagName("Object")
    for widget in widgets:
        xml_result_text.insert("end", "name:"+widget.getAttribute("name"))
        type_str = get_widget_type_str(widget)
        xml_result_text.insert("end", " --- " + "type:" + type_str + '\n' + '\n')
        widget_sum = widget_sum + 1
    xml_result_text.insert("end", "*********** 总数是%d ***********" % widget_sum + '\n')


def get_point_type_widget_list(type_str):
    widget_list = []
    widgets = root_node.getElementsByTagName("Object")
    for widget in widgets:
        type_str = get_widget_type_str(widget)
        if type_str == type_str:
            widget_list.append(widget)
    return widget_list


def readLayer():
    xml_result_text.insert("end", "****所有Layer信息****" + '\n')
    layer_list = get_point_type_widget_list("Layer")
    for ls in layer_list:
        xml_result_text.insert("end", "name:" + ls.getAttribute("name") + '\n')
    xml_result_text.insert("end", "****************" + '\n')


def read_point_list(type_str):
    xml_result_text.insert("end", "****所有%s信息****" % type_str + '\n')
    layer_list = get_point_type_widget_list(type_str)
    for ls in layer_list:
        xml_result_text.insert("end", "name:" + ls.getAttribute("name") + '\n')
    xml_result_text.insert("end", "****************" + '\n')


def get_point_layer_widgets(layer_str):
    widget_list = []
    flag = 0
    layers = root_node.getElementsByTagName("Object")
    for layer in layers:
        type_str = get_widget_type_str(layer)
        if type_str == "Layer":
            if layer.getAttribute("name") == layer_str:
                flag = 1
                continue
            if flag == 1:
                break
        if flag == 1:
            widget_list.append(layer)
    return widget_list


def read_point_layer_widgets(layer_str):
    xml_result_text.insert("end", "****所有%s信息****" % layer_str + '\n')
    widget_list = get_point_layer_widgets(layer_str)
    for ls in widget_list:
        xml_result_text.insert("end", "name:" + ls.getAttribute("name") + '\n')
    xml_result_text.insert("end", "****************" + '\n')


def get_point_widget_type_widgets(widget_str, s_type_str, d_type_str):
    widget_list = []
    flag = 0
    layers = root_node.getElementsByTagName("Object")
    for layer in layers:
        type_str = get_widget_type_str(layer)
        if type_str == s_type_str:
            if layer.getAttribute("name") == widget_str:
                flag = 1
                continue
            if flag == 1:
                break
        if flag == 1:
            if type_str == d_type_str:
                widget_list.append(layer)
            if type_str == "Layer":
                break
    return widget_list


def read_point_widgets(widget_str, s_type_str, d_type_str):
    xml_result_text.insert("end", "****%s下类型为%s的有****" % (widget_str, d_type_str) + '\n')
    widget_list = get_point_widget_type_widgets(widget_str, s_type_str, d_type_str)
    for ls in widget_list:
        xml_result_text.insert("end", "name:" + ls.getAttribute("name") + '\n')
    xml_result_text.insert("end", "****************" + '\n')


def save_xml_data(d_xml_path):
    f = open(d_xml_path, 'w', encoding='utf-8')
    dom_tree.writexml(f, encoding='utf-8')
    f.close()


def del_xml_head(d_xml_path):
    f = open(d_xml_path, 'r+', encoding='utf-8')
    all_the_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        f.write(line.replace('<?xml version="1.0" encoding="utf-8"?>', ''))
    f.close()


def change_point_widgets_name(widget_str, s_type_str, d_type_str, number, change_lists, start_id, end_id):
    """
    修改指定控件下的指定类型的name，仅针对，规律性的递增修改
    :param widget_str: 指定的控件
    :param s_type_str: 指定控件的类型
    :param d_type_str: 要修改的控件的类型
    :param number: 修改的数量
    :param change_lists: 修改的内容列表，"None"时为不修改
    :param start_id: 修改的开始下标
    :param end_id: 修改的结束下标
    """
    i = start_id
    j = 0
    xml_result_text.insert("end", "*****%s改写%s*****" % (widget_str, d_type_str) + '\n')
    widget_list = get_point_widget_type_widgets(widget_str, s_type_str, d_type_str)
    for ls in widget_list:
        # xml_result_text.insert("end", "name:" + ls.getAttribute("name") + '\n')
        j = j + 1
        if j > number:
            j = 1
            i = i + 1
            if i > end_id:
                break
        xml_result_text.insert("end", "old_name:" + ls.getAttribute("name") + '\n')
        if change_lists[j - 1] == "None":
            xml_result_text.insert("end", "new_name:" + ls.getAttribute("name") + '\n')
            continue
        new_name = str(change_lists[j - 1]) + str(i)
        ls.setAttribute("name", new_name)
        xml_result_text.insert("end", "new_name:" + ls.getAttribute("name") + '\n')
        widgets = ls.getElementsByTagName("Property")
        for widget in widgets:
            if widget.getAttribute("name") == "Name":
                widget.childNodes[0].nodeValue = new_name
    save_xml_data(xml_path)
    del_xml_head(xml_path)
    xml_result_text.insert("end", "****************" + '\n')


def change_point_widgets_func(widget_str, s_type_str, d_type_str, func_number, number, change_lists, start_id, end_id):
    """
    修改指定控件下的指定类型的name，仅针对，规律性的递增修改
    :param widget_str: 指定的控件
    :param s_type_str: 指定控件的类型
    :param d_type_str: 要修改的控件的类型
    :param func_number: 要修改的第几个func
    :param number: 修改的数量
    :param change_lists: 修改的内容列表，"None"时为不修改
    :param start_id: 修改的开始下标
    :param end_id: 修改的结束下标
    """
    i = start_id
    j = 0
    xml_result_text.insert("end", "*****%s改写%s的func%d*****" % (widget_str, d_type_str, func_number) + '\n')
    widget_list = get_point_widget_type_widgets(widget_str, s_type_str, d_type_str)
    for ls in widget_list:
        j = j + 1
        if j > number:
            j = 1
            i = i + 1
            if i > end_id:
                break
        if change_lists[j - 1] == "None":
            continue
        xml_result_text.insert("end", "name:" + ls.getAttribute("name") + '\n')
        func_name = "Action" + ("%02d" % func_number)
        new_str = str(change_lists[j - 1]) + str(i)
        widgets = ls.getElementsByTagName("Property")
        for widget in widgets:
            if widget.getAttribute("name") == func_name:
                widget.childNodes[0].nodeValue = new_str
    save_xml_data(xml_path)
    del_xml_head(xml_path)
    xml_result_text.insert("end", "****************" + '\n')


def result_clear_func():
    xml_result_text.delete(1.0, "end")


def xml_path_is_empty():
    global dom_tree, root_node
    path = xml_path_text.get(1.0, "end")[:-1]
    if path == "":
        tkinter.messagebox.showinfo(title="注意", message="没有选择文件")
        return True
    xml_result_text.delete(1.0, "end")
    dom_tree = parse(path)
    root_node = dom_tree.documentElement
    return False


def text_is_empty(text):
    if text.get(1.0, "end")[:-1] == "":
        tkinter.messagebox.showinfo(title="注意", message=str(text)+"没有输入")
        return True
    return False


def input_frame_display(number):
    for i in range(0, 8):
        input_str_frame[i].pack_forget()

    if number == "1":
        pass
    if number == "2":
        pass
    if number == "3":
        pass
    if number == "4":
        input_str_frame[0].pack()
    if number == "5":
        input_str_frame[0].pack()
        input_str_frame[1].pack()
        input_str_frame[2].pack()
    if number == "6":
        input_str_frame[0].pack()
        input_str_frame[1].pack()
        input_str_frame[2].pack()
        input_str_frame[3].pack()
        input_str_frame[5].pack()
        input_str_frame[6].pack()
        input_str_frame[7].pack()
    if number == "7":
        input_str_frame[0].pack()
        input_str_frame[1].pack()
        input_str_frame[2].pack()
        input_str_frame[3].pack()
        input_str_frame[4].pack()
        input_str_frame[5].pack()
        input_str_frame[6].pack()
        input_str_frame[7].pack()


def combobox_choose_func(*args):
    # if xml_path_is_empty():
    #     return
    number = xml_func_combobox.get()[:1]
    input_frame_display(number)


def result_confirm_func():
    if xml_path_is_empty():
        return
    number = xml_func_combobox.get()[:1]
    if number == "1":
        readXML()

    if number == "2":
        read_type_list()

    if number == "3":
        readLayer()

    if number == "4":
        if text_is_empty(input_str_text[0]):
            return
        read_point_layer_widgets(input_str_text[0].get(1.0, "end")[:-1])

    if number == "5":
        if text_is_empty(input_str_text[0]) or text_is_empty(input_str_text[1]) or text_is_empty(input_str_text[2]):
            return
        read_point_widgets(input_str_text[0].get(1.0, "end")[:-1], input_str_text[1].get(1.0, "end")[:-1],
                           input_str_text[2].get(1.0, "end")[:-1])

    if number == "6":
        if text_is_empty(input_str_text[0]) or text_is_empty(input_str_text[1]) or text_is_empty(input_str_text[2])\
                or text_is_empty(input_str_text[3]) or text_is_empty(input_str_text[5]) \
                or text_is_empty(input_str_text[6]) or text_is_empty(input_str_text[7]):
            return
        change_point_widgets_name(input_str_text[0].get(1.0, "end")[:-1], input_str_text[1].get(1.0, "end")[:-1],
                                  input_str_text[2].get(1.0, "end")[:-1], int(input_str_text[3].get(1.0, "end")[:-1]),
                                  input_str_text[5].get(1.0, "end")[:-1].split(','),
                                  int(input_str_text[6].get(1.0, "end")[:-1]),
                                  int(input_str_text[7].get(1.0, "end")[:-1]))

    if number == "7":
        if text_is_empty(input_str_text[0]) or text_is_empty(input_str_text[1]) or text_is_empty(input_str_text[2]) \
                or text_is_empty(input_str_text[3]) or text_is_empty(input_str_text[4]) \
                or text_is_empty(input_str_text[5]) or text_is_empty(input_str_text[6]) \
                or text_is_empty(input_str_text[7]):
            return
        change_point_widgets_func(input_str_text[0].get(1.0, "end")[:-1], input_str_text[1].get(1.0, "end")[:-1],
                                  input_str_text[2].get(1.0, "end")[:-1], int(input_str_text[3].get(1.0, "end")[:-1]),
                                  int(input_str_text[4].get(1.0, "end")[:-1]),
                                  input_str_text[5].get(1.0, "end")[:-1].split(','), # 有问题
                                  int(input_str_text[6].get(1.0, "end")[:-1]),
                                  int(input_str_text[7].get(1.0, "end")[:-1]))


def get_file_name():
    global xml_path_text
    dir_name = askopenfilename()
    print(dir_name)
    xml_path_text.delete(1.0, "end")
    xml_path_text.insert(1.0, str(dir_name))


def init_func_input(input_frame):
    global input_str_frame, input_str_text, input_str_label
    str_list = ["widget名字", "源类型", "目标类型", "不同的个数", "第几个", "替换的数据", "替换的开始ID", "替换的结束ID"]
    for i in range(0, 8):
        input_str_frame[i] = tkinter.Frame(input_frame, width=100, height=1)
        input_str_label[i] = tkinter.Label(input_str_frame[i], width=10, height=1, text=str_list[i])
        input_str_label[i].pack(side=tkinter.LEFT)
        input_str_text[i] = tkinter.Text(input_str_frame[i], width=50, height=1)
        input_str_text[i].pack(side=tkinter.RIGHT)


def init_ui(init_window_name):
    global xml_path_text, xml_result_text, xml_func_combobox, xml_input_frame
    # 文件选择框
    xml_path_frame = tkinter.Frame(init_window_name, width=400, height=1)
    xml_path_frame.pack()
    xml_path_text = tkinter.Text(xml_path_frame, width=100, height=1)
    xml_path_text.pack(side=tkinter.LEFT)
    xml_path_button = tkinter.Button(xml_path_frame, width=5, height=1, text="...", command=get_file_name)
    xml_path_button.pack(side=tkinter.RIGHT)
    # 下拉框
    xml_func_combobox_value_str = tkinter.StringVar()
    xml_func_combobox = ttk.Combobox(init_window_name, width=50, textvariable=xml_func_combobox_value_str,
                                     state="readonly")
    xml_func_combobox['values'] = ("1:读xml所有widget", "2:读类型列表", "3:读xml所有layer", "4:读指定Layer里面的所有控件",
                                   "5、读指定控件里面的指定类型的控件", "6、修改指定控件里面的指定类型的控件的名字",
                                   "7、修改指定控件里面的指定类型的控件的功能名")
    xml_func_combobox.current(0)
    xml_func_combobox.bind("<<ComboboxSelected>>", combobox_choose_func)
    xml_func_combobox.pack()
    # 输入参数
    xml_input_frame = tkinter.Frame(init_window_name)
    init_func_input(xml_input_frame)
    xml_input_frame.pack()
    # 按键
    xml_result_confirm_button = tkinter.Button(init_window_name, width=5, height=1, text="确认", command=result_confirm_func)
    xml_result_confirm_button.pack()
    xml_result_label = tkinter.Label(init_window_name, text="输出")
    xml_result_label.pack()
    xml_result_clear_button = tkinter.Button(init_window_name, width=5, height=1, text="清除", command=result_clear_func)
    xml_result_clear_button.pack()
    # 输出框
    xml_result_text = tkinter.scrolledtext.ScrolledText(init_window_name, width=50, height=30)
    xml_result_text.pack(fill=tkinter.Y)


if __name__ == '__main__':
    # read_point_widgets("sceneLayerMidCoverFlow", "CoverFlow", "CheckBox")
    # change_list = ["sceneLayerCheckBox", "None"]
    # change_point_widgets_name("sceneLayerMidCoverFlow", "CoverFlow", "CheckBox", 2, change_list, 1, 32)
    # change_list = ["Function,MouseUp,SceneLayerCheckBoxOnPress,", "None"]
    # change_point_widgets_func("sceneLayerMidCoverFlow", "CoverFlow", "CheckBox", 1, 2, change_list, 1, 32)
    while 1:
        pass

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
import xlwt
import xlrd
import translate
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

dir_name = ""
input_xml_dir = ""
input_excel_dir = ""
save_flag = 0
write_flag = 0

workbook = xlwt.Workbook(encoding="UTF-8", style_compression=0)
sheet = workbook.add_sheet('test', cell_overwrite_ok=True)
style = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5
style.pattern = pattern
borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
style.borders = borders


def choose_handle():
    global dir_name
    dir_name, filetype = QFileDialog.getOpenFileName(filter="xml Files (*.xml)")  # 设置文件扩展名过滤,注意用双分号间隔
    print(dir_name, filetype)
    ui.textBrowser.setText(dir_name)


def check_handle():
    global dir_name, save_flag
    if dir_name == "":
        return False
    ui.textEdit.setText("")
    tree = ET.parse(dir_name)
    root = tree.getroot()
    print(root.tag, ":", root.attrib)
    widget_sum = 0
    show_flag = 0
    text_str = []
    text_name_list = ["Text1", "Text2", "Text3", "Text4", "Text5", "Text6",
                      "Text7", "Text8", "Text9", "Text10", "Text11"]
    name_str_list = ["控件", "简中", "繁中", "小英", "大英", "俄语", "法语", "意大利语", "塞尔维亚",
                     "西班牙", "捷克语", "乌克兰", "土耳其"]
    for i in range(0, len(name_str_list)):
        sheet.write(0, i, name_str_list[i], style)

    layers = root.findall("Object")
    # print(layers)
    for layer in layers:
        # print(layer.attrib.get("name"))
        widget_sum += 1
        ui.textEdit.append(layer.attrib.get("name") + "\n")
        sheet.write(widget_sum, 0, layer.attrib.get("name"), style)
        widgets = layer.iter("Object")
        for widget in widgets:
            # print(widget.attrib.get("name"))
            attrs = widget.findall("Property")
            text_str = []
            for attr in attrs:
                if attr.attrib.get("name") in text_name_list:
                    if attr.text is not None:
                        text_str.append(attr.text)
                    else:
                        text_str.append(" ")

                if attr.attrib.get("name") == "Text":
                    if attr.text is not None:
                        show_flag = 1
                        text_str.insert(0, attr.text)
                        print(attr.text)

                if show_flag == 1:
                    if attr.attrib.get("name") == "Name":
                        text_name = attr.text
                        print(attr.text)
                        show_flag = 0
                        widget_sum += 1
                        for num in range(0, 13):
                            if num == 0:
                                ui.textEdit.append(name_str_list[num] + ":" + text_name)
                                sheet.write(widget_sum, 0, text_name)
                            else:
                                ui.textEdit.append(name_str_list[num] + ":" + text_str[num-1])
                                sheet.write(widget_sum, num, text_str[num-1])
                        ui.textEdit.append("\n")

    ui.textEdit.append("总数:" + str(widget_sum) + "\n")
    save_flag = 1


def create_dir_path_name(input_dir_name):
    i = 0
    end_num = 0
    while input_dir_name[i] != '/':
        if input_dir_name[i] == '.':
            end_num = i
        i -= 1
    save_path = input_dir_name[:i + 1]
    save_name = input_dir_name[i + 1:end_num]
    print(save_path)
    print(save_name)
    return save_path, save_name


def create_handle():
    global dir_name, save_flag
    if save_flag != 1:
        ui.textEdit.append("无法生成，原因：没有检测！" + "\n")
        return
    save_flag = 0
    save_path, save_name = create_dir_path_name(dir_name)
    workbook.save(save_path + save_name + ".xls")
    ui.textEdit.append("生成成功，文件选择的文件的目录下！" + "\n")


def choose_execl_handle():
    global input_excel_dir
    input_excel_dir, filetype = QFileDialog.getOpenFileName(filter="excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
    print(input_excel_dir, filetype)
    ui.textBrowser_2.setText(input_excel_dir)


def choose_xml_handle():
    global input_xml_dir
    input_xml_dir, filetype = QFileDialog.getOpenFileName(filter="xml Files (*.xml)")  # 设置文件扩展名过滤,注意用双分号间隔
    print(input_xml_dir, filetype)
    ui.textBrowser_3.setText(input_xml_dir)


def replace_xml_handle():
    global input_xml_dir, input_excel_dir
    if input_xml_dir == "" or input_excel_dir == "":
        return False
    rd = xlrd.open_workbook(input_excel_dir)
    rd_sheet = rd.sheet_by_index(0)
    row_sum = rd_sheet.nrows
    print(row_sum)
    ui.textEdit_2.setText("row_sum = %d" % row_sum)
    tree = ET.parse(input_xml_dir)
    root = tree.getroot()
    print(root.tag, ":", root.attrib)
    widget_sum = 1
    text_name_list = ["Text1", "Text2", "Text3", "Text4", "Text5", "Text6",
                      "Text7", "Text8", "Text9", "Text10", "Text11"]
    name_str_list = ["控件", "简中", "繁中", "小英", "大英", "俄语", "法语", "意大利语", "塞尔维亚",
                     "西班牙", "捷克语", "乌克兰", "土耳其"]
    layers = root.findall("Object")
    # print(layers)
    for layer in layers:
        # print(layer.attrib.get("name"))
        widget_sum += 1
        ui.textEdit_2.append("\n" + layer.attrib.get("name"))
        widgets = layer.iter("Object")
        for widget in widgets:
            # print(widget.attrib.get("name"))
            attrs = widget.findall("Property")
            for attr in attrs:
                if attr.attrib.get("name") == "Text":
                    if attr.text is not None:
                        # print(attr.text)
                        if attr.text != rd_sheet.cell_value(widget_sum, 1):
                            old_text = attr.text
                            attr.text = rd_sheet.cell_value(widget_sum, 1)
                            # ui.textEdit_2.append("\n")
                            ui.textEdit_2.append(widget.attrib.get("name") + "的" + name_str_list[1] +
                                                 "由原来的：" + old_text +
                                                 ", 替换为：" + attr.text)

                        for attr1 in attrs:
                            if attr1.attrib.get("name") in text_name_list:
                                num = int(attr1.attrib.get("name")[4:]) + 1
                                if attr1.text != rd_sheet.cell_value(widget_sum, num):
                                    if attr1.text is None and rd_sheet.cell_value(widget_sum, num) == " ":
                                        continue
                                    old_text = attr1.text
                                    attr1.text = rd_sheet.cell_value(widget_sum, num)
                                    # ui.textEdit_2.append("\n")
                                    ui.textEdit_2.append(widget.attrib.get("name") + "的" + name_str_list[num] +
                                                         "由原来的：" + old_text +
                                                         ", 替换为：" + attr1.text)
                                if attr1.attrib.get("name") == text_name_list[-1]:
                                    break

                        widget_sum += 1

    ui.textEdit_2.append("总数:" + str(widget_sum) + "\n")
    out_path, out_name = create_dir_path_name(input_xml_dir)
    tree.write(out_path + "output.xml", encoding="utf-8-sig", xml_declaration=True)
    ui.textEdit_2.append("生成了:" + out_path + "output.xml")


def sure_handle():
    global input_xml_dir
    out_path, out_name = create_dir_path_name(input_xml_dir)
    src_file_name = out_path + "output.xml"
    f = open(src_file_name, 'r+', encoding='utf-8')
    all_the_lines = f.readlines()
    f.seek(0)

    f.truncate()
    for line in all_the_lines:
        f.write(line.replace("<?xml version='1.0' encoding='utf-8-sig'?>\n", ''))
    f.close()

    ui.textEdit_2.append("去掉文件的头")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = translate.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.chooseButton.clicked.connect(choose_handle)
    ui.checkButton.clicked.connect(check_handle)
    ui.createButton.clicked.connect(create_handle)
    ui.chooseButton_2.clicked.connect(choose_execl_handle)
    ui.chooseButton_3.clicked.connect(choose_xml_handle)
    ui.replaceButton.clicked.connect(replace_xml_handle)
    ui.sureButton.clicked.connect(sure_handle)
    sys.exit(app.exec_())


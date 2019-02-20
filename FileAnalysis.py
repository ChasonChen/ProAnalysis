# -*- coding: UTF-8 -*-
import os

import Module
from MFile import MFile


def list_dir(path):
    files = os.listdir(path)
    list_libs = ['pro/AutoNews/Rexxar', 'pro/AutoNews/shauto-lintcheck', 'pro/AutoNews/shauto-comment']
    list_modules = []
    for file in files:
        sub_path = path + "/" + file
        if os.path.isdir(sub_path) and is_module(sub_path):
            # print(sub_path)
            module = os.listdir(sub_path)
            for m_file in module:
                m_dir = sub_path + "/" + m_file
                if os.path.isdir(m_dir) and m_file == "src" and sub_path not in list_libs:
                    list_files = get_file_count(m_dir, m_file, [], [], [])
                    print(sub_path)
                    print("Java:", len(list_files.java_files),"Xml:", len(list_files.xml_files),"Img:", len(list_files.img_files))

                    list_modules.append(list_files)
                    # list_modules.append(list_files)
            print()
    # print(list_modules)
    return list_modules


def get_file_count(path, file, list_xml, list_java, list_img):
    if not os.path.isdir(path):
        module_file = MFile()
        module_file.fName = file
        module_file.fPath = path
        if path.endswith('.xml'):
            module_file.fType = 'xml'
            module_file.lines = get_file_lines(path)
            list_xml.append(module_file)
        elif path.endswith('.java'):
            module_file.fType = 'java'
            module_file.lines = get_file_lines(path)
            list_java.append(module_file)
        elif path.endswith('.jpg') or path.endswith('.gif') or path.endswith('.png'):
            module_file.fType = 'res'
            list_img.append(module_file)
    else:
        for file in os.listdir(path):
            get_file_count(path + "/" + file, file, list_xml, list_java, list_img)
    return Module.Module(list_java, list_xml, list_img)


def get_file_lines(path):
    count = 0
    for count, line in enumerate(open(path, encoding='utf-8')): pass
    return count


def has_files(path):
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(path + "/" + file):
            return True


def is_module(dir):
    files = os.listdir(dir)
    for file in files:
        if file.__contains__("build.gradle"):
            return True

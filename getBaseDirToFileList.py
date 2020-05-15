#!usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
path_list = []
def get_all(path,saveFile=""):
    #path =r'D:\Test3'
    paths = os.listdir(path) # 列出指定路径下的所有目录和文件
    for i in paths:
        com_path = os.path.join(path,i)
        # print(com_path)
        if os.path.isdir(com_path):
            get_all(path=com_path,saveFile=saveFile) # 如果该路径是目录，则调用自身方法
        elif os.path.isfile(com_path):
            path_list.append(com_path) # 如果该路径是文件，则追加到path_list中
            # print(com_path) 打印所有文件的绝对路径
        
        #判断saveFile是否为空
        if len(saveFile) ==0:
            print(com_path) # 打印所有文件和目录的绝对路径
        else:
            #写入指定文件
            with open(saveFile, 'a+') as f:
                print(com_path) # 打印所有文件和目录的绝对路径
                f.write(com_path+"\n")

# 调用函数

#默认的需要处理的目录
needDealDir = r'/www/wwwroot/bw'


#获取用户输入的目录地址
if len(sys.argv) == 2:
    linshipath = sys.argv[1]
    get_all(path=linshipath)
elif len(sys.argv) == 3:
    get_all(path=(sys.argv[1]),saveFile=(sys.argv[2]))
else:
    get_all(path=needDealDir)

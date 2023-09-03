# -*- coding: utf-8 -*-
# @Time    : 2023/9/3 20:21:39
# @Author  : ZMF
# @FileName: nas tools.py.py
# @Software: PyCharm
# @IDE: PyCharm
# @E-Mail: ZZMF20110806@163.com
import hashlib
import os

def require(ModelList):
    NoModel = []
    for Model in ModelList:
        try:
            exec("import " + Model)
        except:
            NoModel.append(Model)
    return NoModel

def usePipInstallWithList(modelList):
    for i in range(len(modelList)):
        os.system("pip install " + modelList[i])

def pause(do='继续', yon=False):
    if yon == True:
        yn = input("是否" + do + "?(y/n)")
    else:
        yn = input("是否" + do + "?")
    if yn == 'y':
        return True
    else:
        return False

def md5(text):
    '''
    :param text: the text you want to MD5
    :return: MD5 text
    '''
    md = hashlib.md5()
    md.update(text.encode("utf-8"))
    return md.hexdigest()

def nprint(text):
    print(text, end='')
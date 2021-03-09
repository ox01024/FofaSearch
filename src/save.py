#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 19:45
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : save.py



def saveJson():
    pass

def savetxt(file_path,result):
    '''
    save result for file
    :param filename:
    :param result:
    :return:
    '''
    with open(file_path,'w') as f:
        for url in result:
            f.write(url + "\n")
    print('file Saved To result folder')




#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 16:41
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : api_f.py
import json
import sys
from src.terminalPrint import printf


def dumpApi(api, file_path='./config/api.json'):
    '''
    dump email and key in Api_file
    :param api: dict {email:?,key:?}
    :return:
    '''
    with open(file_path, 'w+') as api_file:
        json.dump(api, api_file)


def loadApi(file_path='./config/api.json'):
    '''
    load dict in apifile.json
    :param file_path: str apifile_path
    :return: dict apiDict
    '''
    try:
        with open(file_path) as api_f:
            if api_f != None:
                api = json.load(api_f)
                print(api_f)
    except:
        printf('please initialize first or check config file','red')
        sys.exit(1)
    else:
        return api



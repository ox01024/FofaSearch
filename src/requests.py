#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 16:54
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : requests.py
from src.terminalPrint import printf
import requests
import json

def getResponse(api):
    '''

    :param email: str
    :param key: str
    :return: object Response
    '''
    apiUrl='https://fofa.so/api/v1/info/my?'
    email=api['email']
    key=api['key']
    Response=requests.get(apiUrl+'email={}&key={}'.format(email,key))
    if Response.status_code!=200:
        message = 'make sure email and apikey is correct, and level is VIP.'
        printf(message, 'red')
        return False
    else:
        Response_json = json.loads(Response.text)
        message = 'Username:' + Response_json['username'] + '\n'
        message += 'Vip_level:' + str(Response_json['vip_level'])
        print(message)
        return True


#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 19:16
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : core.py
import base64
import requests
from src.save import savetxt
from src.terminalPrint import printf
from src.requests import getResponse
from src.api_f import *

def init(args):
    '''
    Validation information solidification
    https://fofa.so/user/users/detail
    :param email: str,email
    :param key: str,API KEY
    :return:
    '''
    email=args.email
    key=args.key
    # print(email,key)
    api = dict(email=email, key=key)
    initialized = getResponse(api) #Account verification
    if not initialized:
        printf('initializationFailed','red') #Failed
    else:
        dumpApi(api,'./src/config/api.json')
        printf('successfully initialized','green')

def info(args):
    api=loadApi('./src/config/api.json')
    initialization=getResponse(api)
    if not initialization:
        printf('initializationFailed', 'red')  # Failed


def search(args):
    dork=args.dork
    page=args.page
    size=args.size
    fields=args.fields
    full=args.full
    file=args.file
    # target,page=1,size=100,fields='host',full='false'
    queryInterface='https://fofa.so/api/v1/search/all?'
    api=loadApi('./src/config/api.json')
    initialization=getResponse(api)
    if not initialization:
        printf('initializationFailed', 'red')  # Failed
        return
    email=api['email']
    key=api['key']
    dork64=base64.b64encode((dork).encode('utf-8')).decode('utf-8')
    url=queryInterface+'email={}&key={}&qbase64={}&page={}&size={}&fields={}&full={}'.format(email,key,dork64,page,size,fields,full)
    resultResponse=requests.get(url)
    if resultResponse.status_code!=200:
        printf(resultResponse.text,'red')
        return
    result=json.loads(resultResponse.text)
    message='query:'+result['query']+'\n'
    message+='page:'+str(result['page'])+'\n'
    message+='size:'+str(result['size'])
    printf(message,'green')
    results=result['results']
    if file != None:
        file_path = './src/result/' + file + '.txt'
        savetxt(file_path,results)
    else:
        print(results)





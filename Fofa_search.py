#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 10:50
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : Fofa_search.py
from src.terminalPrint import printf
from src.requests import getResponse
from src.api_f import *
from src.terminalPrint import *
import argparse
import json
from src.core import *


def main():
    parser = argparse.ArgumentParser()
    subparsers=parser.add_subparsers()
    # parser_search
    parser_search=subparsers.add_parser(
        'search',
        help='domain,host,ip,header,body,title and == = != =~'
    )
    parser_search.add_argument(
        '-dork',
        help='searchRules'
    )
    parser_search.add_argument(
        '-page',
        default=1,
        help='The number of pages to turn, the default is the first page')
    parser_search.add_argument(
        '-size',
        type=int,
        default=100,
        help='''The number of records returned per query, the default is 100, and the maximum can be set to 10000.
                Note: The body field contains more content, and it is recommended to get ≤100 records each time'''
    )
    parser_search.add_argument(
        '-fields',
        type=str,
        default='host',
        help='''Optional parameter field list, the default is host, separate multiple parameters with commas, such as (fields=ip,title)'''
    )
    parser_search.add_argument(
        '-full',
        type=bool,
        help='The default is false, the default is the same as the page search, only the data within one year can be searched, and the specified as true is searched for all data'
    )
    parser_search.add_argument(
        '-f',
        '--file',
        default=None,
        help='save result in file'
    )
    parser_search.set_defaults(func=search)

    # parser_init
    parser_init=subparsers.add_parser('init',help='Initialize  for fofasearch')
    parser_init.add_argument(
        '-email',
        type=str,
        default='false',
        help='fofa emil'
    )
    parser_init.add_argument(
        '-key',
        type=str,
        help='API KEY ,https://fofa.so/user/users/detail'
    )
    parser_init.set_defaults(func=init)

    # parser_info
    parser_info=subparsers.add_parser('info',help='Show identityInformation')
    parser_info.set_defaults(func=info)
    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        parser.print_help()



if __name__ == '__main__':

    main()



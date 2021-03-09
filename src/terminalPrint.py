#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 16:33
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : terminalPrint.py

# def logo():
#     printf('''
#     __           __            _____                                _
#   / _|          / _|          / ____|                              | |
#  | |_    ___   | |_    __ _  | (___     ___    __ _   _ __    ___  | |__
#  |  _|  / _ \  |  _|  / _` |  \___ \   / _ \  / _` | | '__|  / __| | '_ \
#  | |   | (_) | | |   | (_| |  ____) | |  __/ | (_| | | |    | (__  | | | |
#  |_|    \___/  |_|    \__,_| |_____/   \___|  \__,_| |_|     \___| |_| |_|
#
#                                                  关注公众号信安灯塔  ''', 'yellow')

def printf(s, color="white"):
    """
    print result in terminal
    :param s: str, printed string
    :param color: str, printed string color
    :return: Color output
    """
    colors = {
        "red":      '\033[31m',         # red
        "green":    '\033[32m',         # green
        "yellow":   '\033[33m',         # yellow
        "blue":     '\033[34m',         # blue
        "white":    '\033[37m',         # white
    }

    # default end
    default_end = '\033[0m'  # item default end
    print('{}{}{}'.format(colors.get(color, "WHITE"), s, default_end))




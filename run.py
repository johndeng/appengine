#!/usr/bin/env python
# coding=utf-8


import config
from optparse import OptionParser


def command_line():
    """ 解析命令行参数,
        目前支持指定监听端口.
    """

    parser = OptionParser()
    parser.add_option("-p", "--port", dest="port")

    (options, args) = parser.parse_args()
    if options.port:
        setattr(config, "PORT", int(options.port))

# 启动命令行监听
command_line()

from engine import Server, Welcome
Welcome()
Server().run()



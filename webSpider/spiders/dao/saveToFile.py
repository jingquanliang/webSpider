#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-02 08:45:51
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

import time
import os
import codecs

class SaveToFile(object):
    """docstring for saveToFile"""
    def __init__(self):
        super(SaveToFile, self).__init__()

    @classmethod
    def saveToFileAsHtml(cls, file_name, contents):
        print "save file to:"+file_name
        fh = codecs.open(file_name, 'w',encoding="utf-8")
        fh.write(contents)
        fh.close()

    @classmethod
    def saveToFileAsLog(cls, file_name, contents):
        fh = codecs.open(file_name, 'a',encoding="utf-8")
        currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        fh.write(currentTime+'\n')
        fh.write(contents+'\n')
        fh.write('\n')
        fh.close()

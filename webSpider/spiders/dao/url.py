#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-02 16:28:26
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

import os
import codecs
import threading

class urlSave(object):
    """docstring for urlSet"""

    urlSet = set()
    lock = threading.Lock()

    def __init__(self,file_name):
        super(urlSave, self).__init__()
        self.file_name=file_name


    def saveToFileAsLog(self,contents):
        self.lock.acquire()
        if contents not in self.urlSet:
            fh = codecs.open(self.file_name, 'a',encoding="utf-8")
            # currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            # fh.write(currentTime+'\n')
            fh.write(contents+'\n')
            # fh.write('\n')
            fh.close()
            self.urlSet.add(contents)
        self.lock.release()

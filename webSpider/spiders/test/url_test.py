#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-30 14:28:08
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version

import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)
sys.path.insert(0,parentdir)

import unittest
from dao.url import *

class TestUrlSave(unittest.TestCase):

    def test_saveToFile(self):
        url=urlSave("test.txt")
        url.saveToFileAsLog("aa")
        url.saveToFileAsLog("bb")
        url.saveToFileAsLog("cc")
        url.saveToFileAsLog("bb")

if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-02 18:20:28
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

import urllib
proto, rest = urllib.splittype("http://www.baidu.com/11/12.htm")
host, rest = urllib.splithost(rest)
print host
host, port = urllib.splitport(host)
if port is None:
   port = 80
print port

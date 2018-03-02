#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-31 12:16:57
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

#下载网页文件到本地文件夹
import os,urllib2,urllib

#设置下载后存放的存储路径'C:\Users\yinyao\Desktop\Python code'
# path=r'C:\Users\yinyao\Desktop\Python code'
# file_name=r'MSFT.csv'   #文件名，包含文件格式


def find_last(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)
        if position==-1:
            return last_position
        last_position=position


def readFile(dest_file):
    filePathList=[]
    file=open(dest_file)

    for line in file:
        print(line)
        filePathList.append(line)
    return filePathList

#定义下载函数downLoadPicFromURL（本地文件夹，网页URL）
def downLoadPicFromURL(path,URL,fileName):
# """
#     path: 存储路径
#     URL：下载地址
#     filename：存储文件名称
# """
    try:
        urllib.urlretrieve(URL , os.path.join(path,fileName))
    except:
      print '\tError retrieving the URL:', URL

if __name__ == '__main__':
    downLoadURL="http://data.caida.org/datasets/routing/routeviews-prefix2as/2017/09/routeviews-rv2-20170928-1200.pfx2as.gz"
    path=r'D:\DeskTop\caidaFile'
    downLoadPicFromURL(path,downLoadURL,"routeviews-rv2-20170928-1200.pfx2as.gz")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-02 10:09:25
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

from dao.saveToFile import *
from dao.url import *
from dao.subDomain import *
from dao.fileDownLoad import *

import scrapy
import urllib
from scrapy import *

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from webSpider.items import WebspiderLinkItem

from OpenSSL import SSL
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory

class FinancialSpider(CrawlSpider):
    """继承自CrawlSpider，实现自动爬取的爬虫。"""

    name = 'caidaa'

    download_delay = 1
    # make scrapy crawl any site without allowed domains restriction
    allowed_domains = ['caida.org']
    #http://data.caida.org/datasets/routing/routeviews-prefix2as/2017/09/
    #http://data.caida.org/datasets/topology/ark/ipv4/probe-data/team-1/2015/cycle-20151002/
    start_urls = ['http://data.caida.org/datasets/topology/ark/ipv4/probe-data/team-1/2015/cycle-20151002/']

    custom_settings={
        # "DOWNLOADER_CLIENT_TLS_METHOD": SSL.SSLv3,
        "DEFAULT_REQUEST_HEADERS":{
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.8',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.25 Safari/537.36',
        }
    }


    # rules = [
    #     Rule(LinkExtractor(allow=(),
    #          restrict_xpaths=('//a[@href]')),
    #          callback='parse_start_url',
    #          follow=True)
    # ]

    def parse_start_url(self, response):

        item = WebspiderLinkItem()
        sel = Selector(response)

        contentList = response.xpath('//a/@href').extract()
        # print "==============================================================="
        # print contentList

        relativePath=response.url
        # print "11111111111111111111111111111"+relativePath
        proto,rest = urllib.splittype(relativePath)
        host,rest = urllib.splithost(rest) #域名地址
        relativePath = host

        path=r'D:\DeskTop\caidaFile'
        if contentList:
            for link in contentList:
                # save absLink
                if link.startswith("daily.l7.t1"):
                    urlOperate=urlSave("caida.txt")
                    urlOperate.saveToFileAsLog(link)
                    downLoadURL="http://data.caida.org/datasets/topology/ark/ipv4/probe-data/team-1/2015/cycle-20151002/"+link
                    downLoadPicFromURL(path,downLoadURL,link)

                # yield scrapy.Request(absLink)
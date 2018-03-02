#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-02 10:09:25
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

from dao.saveToFile import *
from dao.url import *
from dao.subDomain import *

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

    name = 'longchen'

    download_delay = 1
    # make scrapy crawl any site without allowed domains restriction
    #allowed_domains = ['eastmoney.com']  'http://www.china-longchen.com'
    start_urls = ['https://www.tmall.com/',"https://www.baidu.com/"]

    custom_settings={
        # "DOWNLOADER_CLIENT_TLS_METHOD": SSL.SSLv3,
        "DEFAULT_REQUEST_HEADERS":{
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.8',
            # 'cookie':'_gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_day=1; _gauges_unique_hour=1; _gat=1; censys.io.beaker.session.id=86542fff711c3bd4a3414d73c8b9a61225b03272khUymgQ2F/NfRPHaP4P84l1gA9X5hKhwHv1+5ufn9phVBKMZ6DAu7LBCAYPJJBAl+5fOsgxuuTYU//X50GK0foL44mBjlKjeNDG7qVIhnDHjH+Pyd1uKRU+Y6YcGAP2JUiK+suQYoYfgYtN4V5l0wHNGQ1J62eX90GJz+3a/mV407ACf6o1SpPbFqGBbmyd+wFUhQ+odUShVRSudNuKSoOo/EK9BznAY73Yi8Qep/zOR5Zmpcc/Ayy1E2iVdJMDalDYXgoo9vOB0bTJ1vQKTA6hHSf8ctlRtMaM=; _ga=GA1.2.963336915.1503454419; _gid=GA1.2.2129058772.1504081111',
            # 'upgrade-insecure-requests':'1',
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
        # print contentList

        relativePath=response.url
        # print "11111111111111111111111111111"+relativePath
        proto,rest = urllib.splittype(relativePath)
        host,rest = urllib.splithost(rest) #域名地址
        relativePath = host

        if contentList:
            for link in contentList:
                # link may have the following formula: http://XXX
                # print "55555555555555555555555555555555555:::::"+link
                if ""==link or ":" in link and "http:" not in link: #排除连接中的冒号和空字符串
                    continue
                elif link[0:2]=="//":  # remove the link beginning string "//"
                    link=link[2:]
                elif link[0]=="/": # remove the link beginning string "/"
                    link=link[1:]

                flag,subDomain=getDomain(link)
                if "http://" in link:
                    absLink=link
                elif "https://" in link:
                    absLink=link
                elif flag: #子域名,这时一定没有http或者https了，因为上边的if语句处理了
                    absLink=proto+"://"+link
                elif "./"==link:
                    continue
                else:
                    absLink=proto+"://"+relativePath+"/"+link
                # print "6666666666666666666666666666666666666:::::"+absLink
                item['link'] = absLink
                # print absLink
                urlOperate=urlSave("tmall.txt")
                urlOperate.saveToFileAsLog(absLink)
                if "www.baidu.com/more/"==absLink:
                    print "11111111111111111111111111111"+response.url
                    print "22222222222222222222222222222"+link
                    exit(1)
                yield scrapy.Request(absLink)
                # request=scrapy.Request(absLink)
                # try:
                #     metaInfo=response.meta['host']
                #     print metaInfo+"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&22222222222222222"
                # except Exception as e:
                #     pass
                # request.meta['host'] = "http://www.china-longchen.com"
                # yield request
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-02 08:45:51
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

import scrapy
from scrapy import *
from dao.saveToFile import *
import json

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class tfsSpider(scrapy.Spider):
    name = "tmall"
    allowed_domains = ["tmall.com"]
    # start_urls = ['http://www.censys.io/login']
    custom_settings={
        "DEFAULT_REQUEST_HEADERS":{
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.8',
            # 'cookie':'_gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_day=1; _gauges_unique_hour=1; _gat=1; censys.io.beaker.session.id=86542fff711c3bd4a3414d73c8b9a61225b03272khUymgQ2F/NfRPHaP4P84l1gA9X5hKhwHv1+5ufn9phVBKMZ6DAu7LBCAYPJJBAl+5fOsgxuuTYU//X50GK0foL44mBjlKjeNDG7qVIhnDHjH+Pyd1uKRU+Y6YcGAP2JUiK+suQYoYfgYtN4V5l0wHNGQ1J62eX90GJz+3a/mV407ACf6o1SpPbFqGBbmyd+wFUhQ+odUShVRSudNuKSoOo/EK9BznAY73Yi8Qep/zOR5Zmpcc/Ayy1E2iVdJMDalDYXgoo9vOB0bTJ1vQKTA6hHSf8ctlRtMaM=; _ga=GA1.2.963336915.1503454419; _gid=GA1.2.2129058772.1504081111',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.25 Safari/537.36',
        }
    }

    def start_requests(self):
        params={
            "language":"",
            "USER":"TFSRU_TFSRUjhxKF",
            "ACCOUNT":"TFSRUjhxKF",
            "PASSWORD":"TFSRUjhxKF",
            "COMPANY":"TFSRU"
        }
        return [scrapy.FormRequest("http://47.89.36.24:8088/escm/loginDiy.sc",formdata=params,method='POST',callback=self.after_login,errback=self.errback_httpbin)]
        # return [Request("http://www.censys.io/login", callback = self.post_login)]

    def after_login(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        # pass
        html=response.body
        SaveToFile.saveToFileAsHtml("tfs.html",html)



    def parse(self, response):
        html=response.body
        SaveToFile.saveToFileAsHtml("account.html",html)

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

    def post_login(self,response):

        print 'Preparing login'
        #下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        csrf_token = Selector(response).xpath('//input[@name="csrf_token"]/@value').extract()[0]
        # csrf_token=response.body.get_csrf_token()
        print("csrf_token:"+csrf_token)
        params={"login":"jingquanliang",
                  "password":"1qaz2wsx",
                  "came_from":"/",
                  "csrf_token":csrf_token
                }
        # ,cookies=self.cookies, meta={'cookiejar': 1}
        print "===================================================================="
        # print response.headers
        print "===================================================================="
        print response.status
        print response.request.url
        print response.flags
        print "===================================================================="
        # print response.meta['cookiejar']
        # response.urljoin("")
        response=response.replace(url="https://www.censys.io/login")
        print response.url
        return [scrapy.FormRequest.from_response(response,formdata=params,method='POST',callback=self.after_login)]


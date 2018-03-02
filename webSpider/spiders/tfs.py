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
    name = "tfs"
    allowed_domains = ["tfs906wms.com"]
    # start_urls = ['http://www.censys.io/login']

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


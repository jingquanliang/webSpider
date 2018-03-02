# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#


from scrapy import *
import scrapy
from scrapy import signals


class redirectMiddleware(object):

    def process_request(self,request, spider):
        #

        # # print "=========================in redirectMiddleware process_request start=========================================="
        # myurl=request.url
        # # print "befor replace:"+myurl+"\n"
        # if "ipv4" in myurl:
        #     # urlList=myurl.split("?")
        #     p=myurl.find("&")
        #     params=myurl[p:-1]
        #     # print myurl[p:-1]+"\n"
        #     realURL="https://www.censys.io/login"
        #     # realURL="http://www.censys.io/login"+params
        #     modifyRequest=request.replace(url=realURL)
        #     myurl=modifyRequest.url
        #     # print "after replace:"+myurl+"\n"
        #     # print modifyRequest.headers
        #     return modifyRequest
        # # print "=========================in redirectMiddleware process_request end==========================================="
        # return None
        return request

    def process_response(self,request, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # print "=========================in redirectMiddleware process_response==========================================="
        # print response.headers
        # print "=========================in redirectMiddleware process_response==========================================="
        return response


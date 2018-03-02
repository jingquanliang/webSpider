# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#


import scrapy.downloadermiddlewares.DownloaderMiddleware


class redirectMiddleware(DownloaderMiddleware):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def process_request(request, spider):
        # This method is used by Scrapy to create your spiders.

        return request

    def process_response(request, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        print "=========================in redirectMiddleware==========================================="
        print response.headers
        return response
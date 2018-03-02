# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy
from scrapy import *
from dao.saveToFile import *
import json

class CensyscrawlSpider(scrapy.Spider):
    name = "censys"
    allowed_domains = ["censys.io"]
    # start_urls = ['http://www.censys.io/login']

    def start_requests(self):
        return [Request("http://www.censys.io/login", callback = self.post_login)]


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

    def after_login(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        # pass
        html=response.body
        SaveToFile.saveToFileAsHtml("censys.html",html)

        # return [Request("https://www.censys.io/account", callback = self.parse)]
        cookies="""_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; auth_tkt="4b5ba016b6f50320502ce26bf1770e9dae2558009e826ee9daeb037d9c5965540b1b172ce9c100d7ed5705155a4bd6ae112f9d6ea4afcef06d29c3e6dbf4d72e59a8d48damluZ3F1YW5saWFuZw%3D%3D!userid_type:b64unicode"; auth_tkt="4b5ba016b6f50320502ce26bf1770e9dae2558009e826ee9daeb037d9c5965540b1b172ce9c100d7ed5705155a4bd6ae112f9d6ea4afcef06d29c3e6dbf4d72e59a8d48damluZ3F1YW5saWFuZw%3D%3D!userid_type:b64unicode"; censys.io.beaker.session.id=70854f2138ac2b54a9b2996f12bfc0ae6fdde365uS2IsQ9HyGbq1k/5yksXYUi1CCaOD03qvwC4/qGg/T+xGtKUsJb5W67UfYmfQTLhm2P20Zzxo/ecGVJgiSlSrccD98J6sjChbFEi3HJzhCRfRBll4WzGZtPaQ2IjNiMeDVBvRwVMxA/bRX+kMtuPqc66dVlNjkZTsTq5mmLVIWpxuUUyRErkoalsybW1fo93y/WJ9U2QtcHKV7GK/K711AAw/xW33XMd8Uf94RNP0jEZhMJRM7QU0B8LZD9aTM1CGYHgR4ZRcKwHM2VWUAdl8TTUA6jTgXTDn8w=; _ga=GA1.2.963336915.1503454419; _gid=GA1.2.2129058772.1504081111; _gat=1"""
        return [FormRequest("https://www.censys.io/account",callback=self.parse)]



    def parse(self, response):
        html=response.body
        SaveToFile.saveToFileAsHtml("account.html",html)

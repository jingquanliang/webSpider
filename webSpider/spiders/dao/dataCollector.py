#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 15:33:33
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : 0.1

import os

import sys
import json
import requests
import time

class DataCollector(object):
    """docstring for getData
    """
    def __init__(self, API_URL,UID,SECRET,paramsData):
        super(DataCollector, self).__init__()
        self.API_URL = API_URL
        self.UID=UID
        self.SECRET=SECRET
        self.paramsData=paramsData


    def getData(self):
        # print(json.dumps(paramsData)["query"])
        res = requests.post(self.API_URL, auth=(self.UID, self.SECRET),data=json.dumps(self.paramsData))
        print res.text
        if res.status_code != 200:
            print "error occurred: %s" % res.status_code
        else:
            print("create job success!")
            res = res.json()
            job_id=res["job_id"]
            self.saveToFile("job-id.txt",job_id)
            return job_id

    @classmethod
    def saveToFile(cls, file_name, contents):
        fh = open(file_name, 'a')
        currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        fh.write(currentTime+'\n')
        fh.write(contents+'\n')
        fh.write('\n')
        fh.close()

    def getJobStatus(self):
        while True:
            res = requests.get(self.API_Get_URL, auth=(self.UID, self.SECRET))
            # print type(res)
            # print type(res.text)

            # res=json.loads(res.text)
            # res = res.json()
            # print type(res)
            # print "job id is :"+res["job_id"]
            if res.status_code == 404 :
                print("he specified job ID was invalid and could not be found.")
            elif  res.status_code == 429 :
                print("The requested record was not retrieved because you have exceeded your specified rate limit.")
            elif  res.status_code != 500 :
                print("""An unexpected error occurred when trying to execute your query.Try again at a later time or contact us at requests@censys.io if the problem persists.""")
            elif res.status_code == 200  :
                print("The job was retreived successfully.")
                break
            else:
                pass
            time.sleep(5)

if __name__ == "__main__":

    API_URL = "https://www.censys.io/api/v1"+"/export"
    UID = "a9cd377f-0144-4376-9820-d5cc25c9ce25"
    SECRET = "Suq8m700V3mFcxFZvtxa3nouIEvhWf2n"

    paramsData={
      # "query":"SELECT location.country, count(ip) FROM ipv4.20170818 GROUP BY location.country;",
      "query":"SELECT * FROM ipv4.20170818 GROUP BY ip.location.country;",
      "format":"json",
      "flatten":False
    }

    dataCollector=DataCollector(API_URL,UID,SECRET,paramsData)
    job_id=dataCollector.getData()
    print("the job id is :"+str(job_id))
    # output = open('job-id.txt', 'w')
    dataCollector.API_Get_URL="https://www.censys.io/api/v1/export/"+job_id
    dataCollector.getJobStatus()


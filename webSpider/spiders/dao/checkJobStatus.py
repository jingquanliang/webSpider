#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-29 11:35:25
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

import os
from dataCollector import *

if __name__ == "__main__":

    API_URL = "https://www.censys.io/api/v1"+"/export"
    UID = "a9cd377f-0144-4376-9820-d5cc25c9ce25"
    SECRET = "Suq8m700V3mFcxFZvtxa3nouIEvhWf2n"

    job_id="""ahZzfnN0ZWFkeS1jaXJjdWl0LTkxNDE3cjsLEhFCaWdRdWVyeUV4ZWN1dGlvbiIkNmExZmRmZDQtOGM2YS0xMWU3LWI5NjEtMGIwN2VjZjE2ODY3DA"""

    paramsData={}


    dataCollector=DataCollector(API_URL,UID,SECRET,paramsData)
    dataCollector.API_Get_URL="https://www.censys.io/api/v1/export/"+job_id
    dataCollector.getJobStatus()
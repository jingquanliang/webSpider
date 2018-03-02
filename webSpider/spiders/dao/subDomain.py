#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-03 13:46:16
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

import re
def getDomain(s):
    '''
        判断s是否一个二级域名，如果是二级域名，返回true 和 二级域名的地址
    '''
    res = s
    # domainS = [".com",".cn",".com.cn",".gov",".net",".edu.cn",".net.cn",".org.cn",".co.jp",".gov.cn",".co.uk","ac.cn",".edu",".tv",".info",".ac",".ag",".am",".at",".be",".biz",".bz",".cc",".de",".es",".eu",".fm",".gs",".hk",".in",".info",".io",".it",".jp",".la",".md",".ms",".name",".nl",".nu",".org",".pl",".ru",".sc",".se",".sg",".sh",".tc",".tk",".tv",".tw",".us",".co",".uk",".vc",".vg",".il",".li",".nz"]
    domainS = ["com","cn","com.cn","gov","net","edu.cn","net.cn","org.cn","co.jp","gov.cn","co.uk","ac.cn","edu","tv","info","ac",".ag",".am",".at",".be",".biz",".bz",".cc",".de",".es",".eu",".fm",".gs",".hk",".in",".info",".io",".it",".jp",".la",".md",".ms",".name","nl","nu","org","pl","ru","sc","se","sg","sh","tc","tk","tv","tw","us","co","uk","vc","vg","il","li","nz"]
    for l in domainS:
        reStr='[^.][\w.]+\.'+l+'/?'
        # if(l==".com"):
        #     print reStr
        matchObj = re.match(reStr,s) #构建正则表达式
        if matchObj:
            subdomain=matchObj.group() # 匹配的完整文本字符，即：matchObj.group(0)
            if subdomain:
                # print l
                return True,subdomain
            else:
                pass
    return False,res

if"__main__":
    print getDomain("i.taobao.com/my_taobao.htm")
    print getDomain("./detail?b=1&c=513&w=%E5%DE%B9%B7%CE%B4%CB%A9%C9%FE%D4%E2%B1%A9%B4%F2")
    print getDomain("#_msocom_1")
    print getDomain("?word=郭德纲相声集锦&ct=301989888&ie=utf-8&ty%3D21%26nf%3D0%26cl%3D0%26du%3D0%26pd%3D0%26sc%3D0%26order%3D1")
    print getDomain("index")
    print getDomain("news/policy/")
    print getDomain("szzw?detailidx=0&city=柳州&id=http%3A%2F%2Fkg.baidu.com%2Fod%2F4002%2F2010458%2Fe8cf814b2a9ba45b4d21096ba80acf&query=手机维修")
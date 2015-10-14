#coding=utf-8
'''
Created on 2015年10月11日

@FileName: G:/GitBackup/Python/Tieba/Tieba_sign/Tieba_sign.py

@Description: (描述) 

@Site:  http://www.sugarguo.com/

@author: 'Sugarguo'

@version V1.0.0
'''


import sys
from time import sleep
sys.path.append("..")

import datetime
import requests
from lxml import etree

times = 3
v = '你的i贴吧v码'
tbs = '你抓包获取的tbs号码'
cookie = '你的COOKIE,要复制全'

url_love = 'http://tieba.baidu.com/f/like/mylike?v=' + v +'&pn='

headers = {'HOST': 'tieba.baidu.com',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate',
           'Connection': 'keep-alive',
        }

f = file('tieba_log.txt','a')
#获得当前时间
now = datetime.datetime.now()
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
f.write('\n\nStart Time :' + str(otherStyleTime) + '\n')
print 'Start Time :' + str(otherStyleTime) + '\n'

def Sign(name):
    data = {'ie':'utf-8',
            'kw':name,
            'tbs':tbs
            }
    url='http://tieba.baidu.com/sign/add'
    try:
        cookies = dict(BDUSS=cookie)
        r = requests.post(url,data=data, headers=headers, cookies=cookies)
        backcontent = r.text.decode('utf-8')
        if '1101' in backcontent:
            print '已经签过到了'
            f.write('%s    已经签过到了\n'%name)
        elif '1102' in backcontent:
            print '你签的太快了'
            f.write('%s    你签的太快了\n'%name)
        elif '2150040' in backcontent:
            print '需要验证码'
            f.write('%s    需要验证码\n'%name)
        else:
            print '签到成功'
            f.write('%s    签到成功\n'%name)
        print backcontent
        f.write(backcontent + '\n')
        return backcontent.decode('utf-8')
    except:
        print("签到    %s    失败" %name)
        f.write("签到%s失败\n" %name)
        return 0

def Get_Html(url):
    #headers["Cookie"] = {'BDUSS':'prTUZVQXpFM3NqNWxRdy1WYWZ0dmhhZzE3cjNrOTl-QXZ6TnA2eXBoeEd-RUZXQVFBQUFBJCQAAAAAAAAAAAEAAAAVLRQDMzUzNDYzNjkyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEZvGlZGbxpWZl',}
    cookies = dict(BDUSS=cookie)
    r = requests.get(url, headers=headers, cookies=cookies)
    print 'status code: ',r.status_code
    print 'encode: ',r.encoding
    html = r.content.decode('gbk','ignore').encode('utf-8')
    #print html
    return html

def GetTitle(html):
    page = etree.HTML(html.lower().decode('utf-8'))
    titles = page.xpath(u'//tr/td[1]/a/text()')
    for item in titles:
        print item
        Sign(item.strip().encode('utf-8'))
        sleep(30)

for num in range(1,times):
    url = url_love + str(num)
    #html = Get_Html(url)
    print url
    GetTitle(Get_Html(url))

now = datetime.datetime.now()
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
f.write('End Time :' + str(otherStyleTime) + '\n\n')
print 'End Time :' + str(otherStyleTime) + '\n'
f.close()
exit()

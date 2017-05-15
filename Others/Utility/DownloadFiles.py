#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '使用python下载文件'
__author__ = '皮'
__mtime__ = '11/29/2015-029'
__email__ = 'pipisorry@126.com'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import requests


def Login1():
    form = {'user': 'brat2015', 'password': 'brat2015'}
    r = requests.get("http://123.57.158.180/~brat/ajax.cgi", params=form)
    print(r.text)


def Login():
    import urllib.request
    import urllib.parse
    import urllib.error
    import http.cookiejar

    LOGIN_URL = 'http://123.57.158.180/~brat/ajax.cgi'
    get_url = 'http://123.57.158.180/~brat/plain_comment/201528015029049_1'  # 利用cookie请求访问另一个网址

    values = {'action': 'login', 'user': 'brat2015', 'password': 'brat2015', 'protocol': '1'}
    postdata = urllib.parse.urlencode(values).encode()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/44.0.2403.157 Safari/537.36'}

    cookie_filename = 'cookie_jar.txt'
    cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie_jar)
    opener = urllib.request.build_opener(handler)

    request = urllib.request.Request(LOGIN_URL, postdata, headers)
    try:
        response = opener.open(request)
        print(response.read().decode())
    except urllib.error.URLError as e:
        print(e.code, ':', e.reason)

    cookie_jar.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    for item in cookie_jar:
        print('Name = ' + item.name)
        print('Value = ' + item.value)

    get_request = urllib.request.Request(get_url, headers=headers)
    get_response = opener.open(get_request)
    print(get_response.read().decode())


def DownloadFiles():
    urls = [r'201528015029049_' + str(i) for i in range(1, 26)]
    for url in urls:
        response = requests.get(url)
        content = response.text
        print(content)
        break


if __name__ == '__main__':
    # Login()
    DownloadFiles()

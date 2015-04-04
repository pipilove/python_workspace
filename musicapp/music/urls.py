#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'LML_CH'
__mtime__ = '2015/3/19'
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
from django.conf.urls import patterns, url

from music import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^page(?P<num>\d+)/$',views.home, name='page'),
    url(r'^play(?P<id>\d+)/$',views.play, name='play'),
    url(r'^hate(?P<id>\d+)/$',views.hate, name='hate'),
    url(r'^love(?P<id>\d+)/$',views.love, name='love'),
    url(r'^explore/$',views.explore, name='explore'),
    url(r'^recommend/$',views.guess, name='recommend'),
    url(r'^search/$',views.search, name = 'search'),
    url(r'^search/page(?P<num>\d+)/$',views.search, name = 'pages'),
    url(r'^login/$',views.login,name='login'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^logout/$',views.logout,name='logout'),
)


#!/usr/bin/env python
#encoding: utf-8

'''
@Author: weilee
@Email: weileemail2016@gmail.com
@File: views.py
@Time: 2018/9/3 上午10:52
'''
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
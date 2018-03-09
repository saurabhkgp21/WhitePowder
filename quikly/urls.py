# -*- coding: utf-8 -*-
# @Author: Saurabh Agarwal
# @Date:   2018-03-09 18:37:55
# @Last Modified by:   Saurabh Agarwal
# @Last Modified time: 2018-03-09 20:47:18
from django.urls import path

from . import views

app_name = 'quikly'

urlpatterns = [
    path('', views.index, name='index'),
]
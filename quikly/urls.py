# -*- coding: utf-8 -*-
# @Author: Saurabh Agarwal
# @Date:   2018-03-09 18:37:55
# @Last Modified by:   Saurabh Agarwal
# @Last Modified time: 2018-03-11 14:16:27
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'quikly'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.SignIn, name='sign_in'),
	url(r'^logout/$', views.LogOut, name='sign_out'),
	url(r'^sign_up/$', views.SignUp, name='sign_up'),
	url(r'^ride/$', views.Ride, name='ride'),
	url(r'^position/$', views.Position, name='position'),
]
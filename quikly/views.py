# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	request.session['name'] = 'x'
	return render(request,'quikly/index.html',{
		'name':'Saurabh'
		})
    # return HttpResponse("Hello, world. You're at the polls index.")

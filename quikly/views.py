# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm

# Create your views here.
def index(request):
	return render(request,'quikly/index.html',{
		'name':'Saurabh'
		})

def SignUp(request):
	if request.method == 'POST':
		form = SignUpForm(data = request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return render(request, 'quikly/index.html')
		else:
			error = form.errors
			new_form = SignUpForm()
			print(error)
			return render(request, 'quikly/sign_up.html', {
				'form':new_form,
				'error':error,
				})
	else:
		form = SignUpForm()
		return render(request, 'quikly/sign_up.html', {'form': form})

def SignIn(request):
	if request.method == 'POST':
		username = request.POST.get('username', '' )
		password = request.POST.get('password', '' )
		user = authenticate( username=username, password=password )
		# The default value when a user is not found is none
		if user is not None :
			login( request, user)
			return render(request, 'quikly/index.html')
		else :
			return render(request, "registration/login.html", {'error':'Invalid Credentials'})
			# Takes back to login page with an error message
	else:
		return render(request, 'registration/login.html')

def LogOut(request):
	logout(request)
	return render(request, 'quikly/index.html')
	
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import QuiklyUser, Cycles
import requests
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request, cycle_available=False):

	if request.method == 'POST':
		print("Request ", request.POST)
		# position = Position(data =request.POST)
		# if position.is_valid():
		# 	position.save()
		# 	print(position.cleaned_data.get('latitude'))
		# 	print(position.cleaned_data.get('longitude'))
		# else:
		# 	print("Position not received")
		cycle_available = request.POST.get('cycle_available','')
		print("Print availability ", cycle_available)
		if cycle_available:
			# cycle_model = request.POST.get('cycle_model','')
			my_id = QuiklyUser.objects.filter(user = request.user)[0]
			my_cycle = my_id.my_cycle
			my_cycle.status = 'Available'
			print("Heree")
			my_cycle.save()
			# send_url = 'http://freegeoip.net/json'
			# r = requests.get(send_url)
			# j = json.loads(r.text)
			# latitude = j['latitude']
			# longitude = j['longitude']
			# longitude = request.POST.get('longitude','')
			# latitude = request.POST.get('latitude','')
			# print(longitude, latitude)
			# Cycles(cycle_model=cycle_model, latitude=latitude,status = 'Available' ,longitude=longitude, owner = owner).save()

		else:
			my_id = QuiklyUser.objects.filter(user = request.user)[0]
			cycle = my_id.my_cycle
			if cycle.status == 'Available':
				cycle.status = 'Not_Available'
				cycle.save()

	if request.user.is_authenticated:
		# position = Position()
		print("Logged in ", request.user.username)
		print("Cycles", len(Cycles.objects.all()))
		for cycle in Cycles.objects.all():
			print(cycle.cycle_model)
		my_id = QuiklyUser.objects.filter(user=request.user)[0]
		# cycles = my_id.my_cycle.all()
		# if len(cycles):
		# 	cycle = cycles[0]
		# 	if cycle.status == 'Available':
		# 		cycle_available = True

		return render(request,'quikly/index.html',{
		'name':'Saurabh',
		'user': request.user,
		'cycle': cycle_available,
		# 'pos':position,
		})
	else:
		print("Not Logged In")
		return render(request,'quikly/index.html',)

def SignUp(request):
	if request.method == 'POST':
		form = SignUpForm(data = request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			phone = request.POST.get('phone','')
			cycle_model = request.POST.get('cycle_model','')
			user = authenticate(username=username, password=raw_password)
			QuiklyUser(user=user, status='LogIn', phone=phone).save()
			login(request, user)
			my_id = QuiklyUser.objects.filter(user=request.user)[0]
			Cycles(owner=my_id, cycle_model=cycle_model, status='Not_Available').save()
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
		print("In sign in")
		username = request.POST.get('username', '' )
		password = request.POST.get('password', '' )
		user = authenticate( username=username, password=password )
		# The default value when a user is not found is none
		if user is not None :
			login( request, user)
			my_id = QuiklyUser.objects.filter(user=user)[0]
			my_id.status = 'LogIn'
			print(my_id.user.username," Number ", my_id.phone)
			my_id.save()
			return HttpResponseRedirect(reverse('quikly:index'))
			# return render(request, 'quikly/index.html')
		else :
			return render(request, "registration/login.html", {'error':'Invalid Credentials'})
			# Takes back to login page with an error message
	else:
		return render(request, 'registration/login.html')

def LogOut(request):
	if request.user.is_authenticated:
		my_id = QuiklyUser.objects.filter(user = request.user)[0]
		my_id.status = 'LogOut'
		my_id.save()
		logout(request)
		print("Log Out")
	return HttpResponseRedirect(reverse('quikly:index'))

def Ride(request):
	lat_x = 22.33
	long_x = 87.30

		
	cycles = Cycles.objects.filter(status='Available')
	for cycle in cycles:
		print(cycle.cycle_model)
	return render(request, 'quikly/ride.html',{
		'user': request.user,
		'cycles': cycles,
		})

@csrf_exempt
def Position(request):
	print("Getting Position")
	if request.method == 'POST':
		latitude = request.POST.get('latitude')
		longitude = request.POST.get('longitude')
		print(latitude, longitude)
		owner = request.user
		my_id = QuiklyUser.objects.filter(user=request.user)
		cycle = my_id.my_cycle.all()[0]
		cycle.latitude = latitude
		cycle.longitude = longitude
		cycle.save()


# @csrf_exempt
# def update_location(request):
# 	if request.method == "POST":
# 		owner = request.user
# 		my_id = QuiklyUser.objects.filter(user=owner)[0]
# 		cycle_model = request.pos
# 		lendituser = request.user.lendituser;
# 		lat = request.POST['latitude']
# 		long = request.POST['longitude']
# 		lendituser.lat = lat
# 		lendituser.long = long
# 		lendituser.save()
# 		return HttpResponseRedirect(reverse('home'))
# 	else:
# 		return HttpResponse("you are here")

# def Share(request):
# 	if request.method == 'POST':
# 		cycle_model = request.POST.get('cycle_model','')
# 		owner = QuiklyUser.objects.filter(user = request.user)[0]
# 		send_url = 'http://freegeoip.net/json'
# 		r = requests.get(send_url)
# 		j = json.loads(r.text)
# 		latitude = j['latitude']
# 		longitude = j['longitude']
# 		Cycles(cycle_model=cycle_model, latitude=latitude,status = 'Available' ,longitude=longitude, owner = owner).save()
# 		return HttpResponseRedirect(reverse('quikly:index'))
# 	else:
# 		if request.user.is_authenticated:
# 			return render(request, 'quikly/share.html')
# 		else:
# 			return HttpResponseRedirect('quikly:sign_in')
	
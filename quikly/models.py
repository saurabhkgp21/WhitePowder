# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Cycles(models.Model):
	STATUS = (('Not_Available', 'Not_Available'), ('Available', 'Available'))
	owner = models.ForeignKey('QuiklyUser', on_delete=models.CASCADE, related_name='my_cycle')
	cycle_model = models.CharField(max_length = 50)
	latitude = models.DecimalField(default=0, decimal_places=5, max_digits=9)
	longitude = models.DecimalField(default=0, decimal_places=5, max_digits=9)
	status = models.CharField(max_length=10, choices=STATUS, default="Not_Available")
		
class QuiklyUser(models.Model):
	STATUS = (('LogIn', 'LogIn'), ('LogOut', 'LogOut'))
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.IntegerField(blank=True, null=True)
	status = models.CharField(max_length=10, choices=STATUS, default="LogOut")

class Ride(models.Model):
    borrower = models.OneToOneField('QuiklyUser', on_delete=models.CASCADE, related_name='borrower') 
    lender = models.OneToOneField('QuiklyUser', on_delete=models.CASCADE, related_name='lender')
    cycle = models.OneToOneField('Cycles', on_delete=models.CASCADE)
    accepted = models.IntegerField(default=0)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

class Users(models.Model):
	user_name = models.CharField(max_length = 100)
	hall = models.CharField(max_length = 100)
	year_of_study = models.IntegerField()
	email = models.EmailField()

class Cycles(models.Model):
	owner = models.CharField(max_length = 100)
	model = models.CharField(max_length = 50)
	
		
		
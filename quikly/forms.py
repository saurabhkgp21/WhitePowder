# -*- coding: utf-8 -*-
# @Author: Saurabh Agarwal
# @Date:   2018-03-10 01:56:14
# @Last Modified by:   Saurabh Agarwal
# @Last Modified time: 2018-03-10 02:29:08
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='First Name', required=False)
    last_name = forms.CharField(max_length=30, help_text='Last Name', required=False)
    email = forms.EmailField(max_length=254, help_text='Email Address', required=False)

    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Login, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        cleaned_data['password'] = ""
        cleaned_data['user'] = user
        return cleaned_data

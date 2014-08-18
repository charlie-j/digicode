# -*- coding: utf-8 -*-

import django.shortcuts
from django.contrib.auth import authenticate, login, logout
import forms

def home(request):
    return django.shortcuts.render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = forms.Login(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None and user.is_active:
                login(request, user)
                return django.shortcuts.redirect('home')
                # Redirect to a success page.
    form = forms.Login(request.POST)
    return django.shortcuts.render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return django.shortcuts.redirect('home')

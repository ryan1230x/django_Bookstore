# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# View for the Home page
def home_view(request):
    return render(request, 'pages/index.html')

# View for the About page
def about_view(request):
    return render(request, "pages/about.html")

# View for the Shop page
def store_view(request):
    return render(request, 'pages/store.html')

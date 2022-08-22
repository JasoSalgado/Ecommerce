# ecommerce.views.py
# Django modules
from django.shortcuts import render

def home(request):


    return render(request, "home.html")
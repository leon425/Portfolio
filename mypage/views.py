from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import HomePage
from django.contrib.auth import get_user_model # get the user list

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    header = HomePage.objects.get(img_name="background_image")
    headers= HomePage.objects.all()
    return render(response, "main/home.html", {"header":header,"headers":headers,})

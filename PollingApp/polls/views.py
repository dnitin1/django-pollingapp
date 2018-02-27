from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request): #request is object
	return HttpResponse ("Hello, world.")

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def contact(request):
    return HttpResponse("hello, contact")

def about(request):
    return HttpResponse("hello, about!")

def profile(request):
    return HttpResponse("hello, profile!")

def domain(request):
    return HttpResponse("hello, domain!")

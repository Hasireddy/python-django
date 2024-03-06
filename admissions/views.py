from django.shortcuts import render
from django.http import HttpResponse
from . import templates

# def say_hello(request):
#     return HttpResponse('Hello world')


def addAdmission(request):
    return HttpResponse("<h1>This is add admission view</h1>")

def say_hello(request):
    return render(request,'hello.html')
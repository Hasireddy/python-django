from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('Hello world')


def addAdmission(request):
    return HttpResponse("<h1>This is add admission view</h1>")

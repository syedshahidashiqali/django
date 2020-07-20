from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def fun1(request):
    return HttpResponse("Hello world!") #  Commented bcoz new way work start



def fun2(request):
    return HttpResponse('Hello Shahid')

def fun3(request):
    return HttpResponse("Hello Sadiq")

def fun4(request):
    return HttpResponse("Hello Malik")

def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}!")
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request,username):
    print(username)
    return HttpResponse("Hello World")

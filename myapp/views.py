def from requests import request
from urllib3 import HTTPResponse


from django.shortcuts import render,HttpResponse
from django.http import HttpResponse


#def home(request):
    return HTTPResponse('hello')
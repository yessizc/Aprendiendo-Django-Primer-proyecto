from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse
from urllib3 import HTTPResponse

# Create your views here.

def index(request):
    return render (request,'planta/index.html')


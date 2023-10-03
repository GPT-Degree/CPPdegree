
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def url_rtrn(request):
    url = 'https://youtube.com'
    response = requests.get(url)
    return HttpResponse(url)
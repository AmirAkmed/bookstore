from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bookstore(response):
    return HttpResponse("Hello, Bookstore")
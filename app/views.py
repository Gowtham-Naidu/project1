from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
    return HttpResponse('<h1>first view created</h1>')
def second(request):
    return HttpResponse('<h1>second view created</h1>')
def third(request):
    return HttpResponse('<h1>third view created</h1>')

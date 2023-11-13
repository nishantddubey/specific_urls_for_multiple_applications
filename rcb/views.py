from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kohli(request):
    return render(request,'virat.html')

def max(request):
    return HttpResponse('<h1> THE BIG SHOW </h1>')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')


def sky(request):
    return HttpResponse('<h1> The Mr. 360 of INIDIA The best T20i batsman </h1>')
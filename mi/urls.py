from django.urls import path
from mi.views import *

app_name = 'something'

urlpatterns = [
    path('rohit/',rohit,name='rohit'),
    path('sky/',sky,name='sky'),
]
from django.urls import path
from rcb.views import *

app_name = 'everything'

urlpatterns = [
    path('kohli/',kohli,name='kohli'),
    path('max/',max,name='max')
]
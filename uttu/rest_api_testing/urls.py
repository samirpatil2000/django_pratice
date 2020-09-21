
from django.urls import path
from django import views
from . import views
#
urlpatterns = [
    path('location/',views.rest_api_testing,name='rest_api_testing'),
 ]
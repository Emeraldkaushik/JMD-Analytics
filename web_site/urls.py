from django.contrib import admin
from django.urls import path,re_path

from web_site.views import *


urlpatterns = [
    path('', Index, name="index"),
  
    
]
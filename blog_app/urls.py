from django.urls import path
from .views import *

app_name = 'App blog'
urlpatterns = [
    path('', blog_list, name='blog_list')
]

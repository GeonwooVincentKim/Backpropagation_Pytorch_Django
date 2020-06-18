from django.urls import path, include
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', index, name='index'),
    path('sub/', sub, name='sub'),
    path('', input, name='input'),
]

from importlib.resources import path

from django.views import View
from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('about', views.about, name= 'about'),
    path('coffee', views.coffee, name= 'coffee'),
]
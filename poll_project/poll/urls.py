from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('addpoll', views.addpoll),
    path('vote', views.vote),
    path('result/<slug:poll_id>/', views.result),
    path('register', views.register),
    path('login', views.login),
    path('profile', views.profile),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('addpoll', views.addpoll,name='addpoll'),
    path('vote/<slug:poll_id>/', views.vote,name='vote'),
    path('result/<slug:poll_id>/', views.result,name='result'),
    path('signup', views.register,name='register'),
    path('login', views.login,name='login'),
    path('profile', views.profile,name='profile'),
    path('logout/',views.logoutUser,name='logout'),
]

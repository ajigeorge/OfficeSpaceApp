from django.urls import path
from .import views
from rest_framework import routers
from django.shortcuts import render

urlpatterns = [

    path('users/',views.user_list),
    path('users/<int:pk>/',views.user_detail),
    path('',views.index, name = 'home'),
    path('login_user',views.login_user),
    # path('management',views.management),
    path('logout_view',views.logout_view,),
]
from django.urls import path
from .import views
from rest_framework import routers
from django.shortcuts import render

urlpatterns = [

    path('users/',views.user_list),
    path('users/<int:pk>/',views.user_detail),

    path('',views.index, name = 'home'),
    path('login_view',views.login_view,name='login_view'),
    path('dashboard',views.dashboard),
    path('create',views.create),
    path('new',views.new),
    # path('dashboard/<int:seat_id>/edit',views.edit),
    # path('dashboard/<int:seat_id>/update',views.update),
    # path('dashboard/<int:seat_id>',views.movie),
    # path('dashboard/<int:seat_id>/delete',views.delete),
    path('logout_view',views.logout_view, name='logout_view'),
]
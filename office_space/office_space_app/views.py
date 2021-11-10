from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('employee_name')
    serializer_class = UserSerializer
from django.shortcuts import render, HttpResponse, redirect
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

from django.urls import reverse
from django.http import HttpResponseRedirect

@csrf_exempt
@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, )

    elif request.method =='POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_NO_CONTENT)

def index(request):
    if not request.user.is_authenticated:
        # return redirect('/')
        return render(request,'index.html')
        # return HttpResponseRedirect(reverse('login_user'))


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/login_view')
        
        else:
            messages.info(request, "Bad Credentials!")
            return redirect('home')

    return render(request,"user_management.html")

def logout_view(request):
    logout(request)
    return redirect('home')

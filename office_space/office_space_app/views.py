from django.shortcuts import render, HttpResponse, redirect
from rest_framework import status
from .models import *
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
    return render(request,'index.html')


def login_view(request):
    if request.method == "POST":
        email_id= request.POST['email_id']
        password = request.POST['password']

        user = authenticate(request, email_id=email_id, password=password)

        if user is not None:
            login(request, user)
            return redirect('/login_view')
        
        else:
            messages.info(request, "Bad Credentials!")
            return redirect('home')

    return render(request,"user_management.html")

def dashboard(request):
    # if 'email_id' not in request.session:
    #     return redirect('/')
    # user = User.objects.get(id=request.session['email_id'])
    # context = {
    #     'user': user,
    # }
    return render(request,'assignment.html',context)

def new(request):
    # if 'email_id' not in request.session:
    #     return redirect('/')
    return render(request,'new_assignment.html')

def create(request):
    # user = User.objects.get(id=request.session['user_id'])
    # Seat.objects.create(
    #     seat_number = request.POST['seat_number'],
    #     seat_type = request.POST['seat_type'],
    #     location_code = request.POST['location_code'],
    #     building_code = request.POST['building_code'],
    #     floor_code = request.POST['floor_code'],
    # )
    # return redirect('/dashboard')
    pass

def logout_view(request):
    logout(request)
    return redirect('home')

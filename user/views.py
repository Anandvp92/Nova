from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as lo , login as li
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .models import CustomUser
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def LogoutUser(request):
    lo(request)
    return redirect('registerpage')



@api_view(["GET"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def register(request):
    users=CustomUser.objects.all()
    value=UserSerializer(users,many=True)
    return Response(value.data)

@api_view(["POST"])
def createUser(request):
    if request.method=="POST":
        user_form=UserSerializer(data=request.data)
        if user_form.is_valid():
            user_form.save()
            return Response({"message":"User created successfully"},status=status.HTTP_200_OK)    
        else:
            return Response({"message":"Invalid data"},status=status.HTTP_404_NOT_FOUND)




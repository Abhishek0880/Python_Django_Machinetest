from django.shortcuts import render
from django.contrib.auth.models import User,Group
from client.models import Client,Project
from rest_framework import viewsets
from .serializers import UserSerializer,GroupSerializer,ClientSerializers,ProjectSerializers
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer


#to show the CLIENTS ON API 
class ClientViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializers
#to show the project details on API
class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializers
from django.contrib.auth.models import User,Group
from client.models import Client,Project
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['url','username','email','groups']
    
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=['url','name']

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields= '__all__'
        # fields= ['id','client_name','created_at','username]

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields= '__all__'


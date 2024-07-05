from api.serializers import ClientSerializers,ProjectSerializers
from .models import Client,Project
from rest_framework import generics
from django.shortcuts import render,redirect,HttpResponse
from .forms import ClientForm,ProjectForm
#Create your views here.
class CreateClient(generics.CreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializers
    '''
def create_client(request):
    if request.method=='POST':
        f=ClientForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=ClientForm
        return render(request,'form.html')
'''
class ClientList(generics.ListAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializers

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers
#to show the project details
class ProjectList(generics.ListAPIView):
    queryset=Project.objects.all()
    serializer_class= ProjectSerializers


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers

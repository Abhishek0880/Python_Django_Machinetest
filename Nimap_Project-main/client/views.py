from api.serializers import ClientSerializer,ProjectSerializer
from .models import Client,Project
from rest_framework import generics
from django.shortcuts import render,redirect,HttpResponse
from .forms import ClientForm,ProjectForm
#Create your views here.
class CreateClient(generics.CreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
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
    serializer_class=ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
#to show the project details
class ProjectList(generics.ListAPIView):
    queryset=Project.objects.all()
    serializer_class= ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

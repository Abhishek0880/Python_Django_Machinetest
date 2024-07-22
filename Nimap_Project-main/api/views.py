from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User,Group
from django.http import HttpResponseRedirect
from client.models import Client,Project
from .models import Project
from rest_framework import viewsets
from .forms import ProjectForm
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,GroupSerializer,ClientSerializer,ProjectSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer


#to show the CLIENTS ON API 
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
        
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            client = get_object_or_404(Client, pk=request.POST.get('client_id'))
            project.client = client
            project.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})
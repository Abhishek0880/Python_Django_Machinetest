from .models import Client,Project,User
from django import forms
from django.contrib.auth.forms import UserCreationForm

'''
class UserForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name','gender','age','email','contact','password1','password2']
        '''

class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'
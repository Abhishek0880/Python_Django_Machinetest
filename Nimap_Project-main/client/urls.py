from django.urls import path
from .views import *

urlpatterns = [
    path('client/',ClientList.as_view()),
    path('createclient/',CreateClient.as_view()),
    path('client/<int:pk>/', ClientDetail.as_view()),
    path('project/',ProjectList.as_view()),
    path('project/<int:pk>/', ProjectDetail.as_view())
]
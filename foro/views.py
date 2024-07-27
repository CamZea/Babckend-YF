from django.shortcuts import render
from rest_framework.views import APIView
#from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import ComunitySerializer, ForoSerializer
from .models import Comunity, Foro
from rest_framework.response import Response
# Create your views here.

class ComunityViewSet(ModelViewSet):
    queryset= Comunity.objects.all()
    serializer_class= ComunitySerializer

class ForoViewSet(ModelViewSet):
    queryset= Foro.objects.all()
    serializer_class= ForoSerializer
   
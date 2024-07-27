from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import check_password
from .serializers import UserSerializer, UserLoginSerializer
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer

class AuthenticationView(APIView):
    def post(self, request):
        user_request= UserLoginSerializer(data= request.data)
    
        if not user_request.is_valid():

            return Response({"message": "Email y/o Contraseña inválido(s)"}) 
        return Response ({'message': 'Usuario valido'})
      
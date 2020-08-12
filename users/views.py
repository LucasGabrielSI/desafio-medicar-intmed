from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from utils import random_string
from .models import User
from .serializers import UserSerializer


class UsersCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        nome = request.data['nome']
        email = request.data['email']
        password = request.data['senha']

        if User.objects.filter(email=email).exists():
            return Response({
                'msg': 'Usuário já existe!',
                'status': status.HTTP_400_BAD_REQUEST
            })
        else:
            new_user = User.objects.create_user(username=random_string(), nome=nome, email=email)
            new_user.set_password(password)
            new_user.save()
            return Response({
                'msg': 'Usuário cadastrado com sucesso!',
                'token': new_user.auth_token.key,
                'status': status.HTTP_201_CREATED
            })


class UsersLogin(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['senha']

        if not email or not password:
            return Response({
                'msg': 'Informe os dados corretamente!',
                status: status.HTTP_400_BAD_REQUEST
            })
        elif User.objects.filter(email=email).exists():
            user = authenticate(password=password, username=email)
            if user:
                return Response({
                    'email': user.email,
                    'nome': user.nome,
                    'token': user.auth_token.key,
                    'status': status.HTTP_200_OK
                })
            else:
                return Response({
                    'msg': 'Email ou senha inválidos, confira as informações e tente novamente.',
                    'status': status.HTTP_400_BAD_REQUEST
                })
        else:
            return Response({
                'msg': 'Não existe usuário cadastrado com esses dados!',
                'status': status.HTTP_400_BAD_REQUEST
            })

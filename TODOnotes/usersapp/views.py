from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserListRetrieveUpdateViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin, GenericViewSet):

    renderer_classes = [JSONRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


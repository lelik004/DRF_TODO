from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, AdminRenderer, BrowsableAPIRenderer

from .models import ToDo, Project
from .serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [AdminRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):

    # renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer

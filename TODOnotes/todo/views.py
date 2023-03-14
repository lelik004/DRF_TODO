from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, AdminRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from .filters import ProjectFilter, ToDoProjectFilter
from .models import ToDo, Project
from .serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [AdminRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoModelViewSet(ModelViewSet):

    # renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoProjectFilter

    '''
    Переопределяем функцию удаления в mixins.DestroyModelMixin, 
    чтобы вместо удаления элемента параметр is_activ принимал False
    '''
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

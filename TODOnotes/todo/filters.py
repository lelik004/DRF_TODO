from django_filters import rest_framework as filters
from .models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    name_of_project = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name_of_project']


class ToDoProjectFilter(filters.FilterSet):

    class Meta:
        model = ToDo
        fields = ['project']

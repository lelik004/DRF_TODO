import rest_framework.serializers
from rest_framework import serializers

from usersapp.models import CustomUser
from usersapp.serializers import CustomUserSerializer
from .models import Project, ToDo

'''
При переопределении переменнной с использованием serializers.StringRelatedField 
поле становится "read only"
'''


class ProjectModelSerializer(serializers.ModelSerializer):
    # group_of_users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('pk', 'name_of_project', 'link_to_repo')


class ToDoModelSerializer(serializers.ModelSerializer):
    created_user = serializers.StringRelatedField()
    project = serializers.StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'


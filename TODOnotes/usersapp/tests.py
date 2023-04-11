import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from mixer.backend.django import mixer

from .models import CustomUser
from .views import UserListRetrieveUpdateViewSet, CustomUserModelViewSet
from todo.models import Project, ToDo
from todo.views import ProjectModelViewSet, ToDoModelViewSet


class TestUserViewSet(TestCase):

    def setUp(self):
        self.name = 'admin'
        self.password = 'geekbtains'
        self.email = 'admin@gb.ru'

        self.data = {'username': 'some_username','first_name': 'fnm' , 'last_name': 'lnm' , 'email': 'gb@gb.ru'}
        self.data_updt = {'username': 'some_username2','first_name': 'fnm2' , 'last_name': 'lnm2' , 'email': 'gb2@gb.ru'}
        self.url = '/api/users/'
        self.admin = CustomUser.objects.create_superuser(username=self.name, email=self.email, password=self.password)


# APIRequestFactory
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = UserListRetrieveUpdateViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        view = CustomUserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        force_authenticate(request, self.admin)
        view = CustomUserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# APIClient
    def test_get_detail(self):
        client = APIClient()
        user = CustomUser.objects.create(**self.data)
        response = client.get(f'{self.url}{user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        client = APIClient()
        admin = self.admin
        user = CustomUser.objects.create(**self.data)
        self.client.login(username=self.name, password=self.password)
        response = client.put(f'{self.url}{user.pk}/', self.data_updt)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        client = APIClient()
        user = CustomUser.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.put(f'{self.url}{user.pk}/', self.data_updt)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

# APITestCase


class TestUserViewAPITestCase (APITestCase):

    def setUp(self):
        self.name = 'admin'
        self.password = 'geekbtains'
        self.email = 'admin@gb.ru'

        self.data = {'username': 'some_username','first_name': 'fnm' , 'last_name': 'lnm' , 'email': 'gb@gb.ru'}
        self.data_updt = {'username': 'some_username2','first_name': 'fnm2' , 'last_name': 'lnm2' , 'email': 'gb2@gb.ru'}
        self.url = '/api/users/'
        self.admin = CustomUser.objects.create_superuser(username=self.name, email=self.email, password=self.password)

    def test_get_list_apitc(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_edit_guest_apitc(self):
    #     user = CustomUser.objects.create(**self.data)
    #     response = self.client.post(f'{self.url}{user.pk}', self.data_updt)
    #     print(f'{self.url}{user.pk}/')
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestProjectViewSet(APITestCase):
    # def setUp(self):
    #     self.user_name = 'usrnm'
    #     self.user_email = 'usr_email'
    #     self.user_password = 'geekbrains'
    #     self.admin_user_name = 'admin_usrnm'
    #     self.admin_email = 'admin_email'
    #     self.admin_password = 'geekbrains'
    #     self.project_url = '/api/projects/'
    #     self.todo_url = '/api/todo/'
    #     self.project_data1 = {
    #         'pk': 1,
    #         'name_of_project': 'project_name',
    #         'link_to_repo': 'github.ru/lesson_8',
    #         # 'group_of_users': self.user_name
    #     }
    #     self.project_data2 = {
    #         'pk': 2,
    #         'name_of_project': 'project_name2',
    #         'link_to_repo': 'github.ru/lesson_8',
    #         # 'group_of_users': self.user_name
    #     }
    #     self.todo_data = {
    #         'project': 'project_1',
    #         'todo_body': 'todo_body_1',
    #         'created_user': self.user_name,
    #         'is_active': True
    #     }

    def test_get_project_list(self):
        response = self.client.get(self.project_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project_guest(self):
        project = Project.objects.create(**self.project_data1)
        response = self.client.post(f'{self.project_url}{project.pk}/', self.project_data2)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Не разобрался почему выдает 400ый ответ
    # def test_create_project_admin(self):
    #     # self.user_name = 'usrnm'
    #     # self.user_email = 'usr_email'
    #     # self.user_password = 'geekbrains'
    #     user = mixer.blend(CustomUser)
    #     self.admin_user_name = 'admin_usrnm'
    #     self.admin_email = 'admin_email'
    #     self.admin_password = 'geekbrains'
    #     self.project_url = '/api/projects/'
    #     # self.project_data1 = {
    #     #     'pk': 1,
    #     #     'name_of_project': 'project_name',
    #     #     'link_to_repo': 'github.ru/lesson_8',
    #     #     # 'group_of_users': user
    #     # }
    #     self.project_data2 = {
    #         'pk': 2,
    #         'name_of_project': 'project_name2',
    #         'link_to_repo': 'github.ru/lesson_8_2',
    #         # 'group_of_users': user
    #     }
    #     project1 = mixer.blend(Project)
    #     project2 = mixer.blend(Project)
    #     self.todo_data = {
    #         'project': project1,
    #         'todo_body': 'todo_body_1',
    #         'created_user': user,
    #         'is_active': True
    #     }
    #
    #     admin = CustomUser.objects.create_superuser(
    #         username=self.admin_user_name,
    #         email=self.admin_email,
    #         password=self.admin_password
    #     )
    #
    #     self.client.login(username=self.admin_user_name, password=self.admin_password, format='json')
    #     print(f'{self.project_url}{project1.pk}/')
    #     response = self.client.put(f'{self.project_url}{project1.pk}/', self.project_data2)
    #     print(response)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTodoViewset(APITestCase):

    def test_updt_todo_admin(self):
        self.user_name = 'usrnm'
        self.user_email = 'usr_email'
        self.user_password = 'geekbrains'
        user = CustomUser.objects.create(
            username=self.user_name,
            email=self.user_email,
            password=self.user_password
        )
        self.admin_user_name = 'admin_usrnm'
        self.admin_email = 'admin_email'
        self.admin_password = 'geekbrains'
        self.todo_url = '/api/todo/'
        self.project_data1 = {
            'pk': 1,
            'name_of_project': 'project_name',
            'link_to_repo': 'github.ru/lesson_8',
            # 'group_of_users': user
        }
        project = Project.objects.create(**self.project_data1)
        self.todo_data = {
            'project': project,
            'todo_body': 'todo_body_1',
            'created_user': user,
            'is_active': True
        }

        todo = ToDo.objects.create(**self.todo_data)
        admin = CustomUser.objects.create_superuser(
            username=self.admin_user_name,
            email=self.admin_email,
            password=self.admin_password
        )
        self.client.login(username=self.admin_user_name, password=self.admin_password)
        response = self.client.put(f'{self.todo_url}{project.pk}/', self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updt_todo_admin_with_mixer(self):
        user = mixer.blend(CustomUser)
        self.admin_user_name = 'admin_usrnm'
        self.admin_email = 'admin_email'
        self.admin_password = 'geekbrains'
        self.todo_url = '/api/todo/'
        project = mixer.blend(Project)
        self.todo_data = {
            'project': project,
            'todo_body': 'todo_body_1',
            'created_user': user,
            'is_active': True
        }

        todo1 = mixer.blend(ToDo)
        todo2 = mixer.blend(ToDo)
        admin = CustomUser.objects.create_superuser(
            username=self.admin_user_name,
            email=self.admin_email,
            password=self.admin_password
        )
        print(todo2)
        self.client.login(username=self.admin_user_name, password=self.admin_password)
        response = self.client.put(f'{self.todo_url}{todo1.pk}/', self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

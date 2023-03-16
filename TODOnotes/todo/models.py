from django.db import models

from usersapp.models import CustomUser


class Project (models.Model):
    name_of_project = models.CharField(max_length=64,  blank=False, verbose_name='Название проекта',)
    link_to_repo = models.URLField(max_length=300, blank=True, verbose_name='Ссылка на репозиторий')
    group_of_users = models.ManyToManyField(CustomUser,  verbose_name='Пользователи проекта')

    def __str__(self):
        return f'{self.name_of_project}'


class ToDo (models.Model):
    project = models.OneToOneField(Project, unique=False, on_delete=models.CASCADE, verbose_name='Название проекта задачи')
    todo_body = models.CharField(max_length=1024, verbose_name='Текст заметки')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Создана',)
    update_at = models.DateTimeField(auto_now=True, editable=False, verbose_name= 'Обновлена',)
    created_user = models.OneToOneField(
        CustomUser, unique=False, on_delete=models.CASCADE, verbose_name='Пользователь создавший задачу',
    )
    is_active = models.BooleanField(default=False, verbose_name='Признак активности',)

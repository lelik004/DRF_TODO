from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, unique=True, verbose_name='email')
    # birthday = models.DateTimeField(blank=True, verbose_name='Дата Рождения')
    department = models.CharField(max_length=64, blank=False, verbose_name='Отдел')
    avatar = models.ImageField(blank=True, verbose_name='Аватар')

    def __str__(self):
        return f'{self.last_name}'



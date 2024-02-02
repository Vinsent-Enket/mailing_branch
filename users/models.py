from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

"""
Атрибуты:
1. email
2. name
3. last name
4. company
5. Permission
6. avatar
7. phone
8. рабочая электронка
9. должность (выбор из готовых)
"""


# Create your models here.
class User(AbstractUser):

    username = None
    self_email = models.EmailField(unique=True, verbose_name='Личная почта')
    work_email = models.EmailField(verbose_name='Рабочая почта', default=self_email)

    name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия пользователя')
    # company = models.ForeignKey
    email_verification_token = models.CharField(max_length=255, verbose_name='Токен для регистрации', **NULLABLE)
    email_is_verify = models.BooleanField(default=False, verbose_name='Емейл верифицирован')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                              related_name='user_set',
                                              related_query_name='user', to='auth.permission',
                                              verbose_name='user permissions')
    # appointment = models.CharField(max_length=50, choices=)
    USERNAME_FIELD = "self_email"
    REQUIRED_FIELDS = []

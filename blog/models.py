from django.db import models
import django
from django.utils import timezone
from pytils.translit import slugify

from config import settings

# Create your models here.
NULLABLE = {'blank': True, 'null': True}
now = django.utils.timezone.now


class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок поста')
    slug = models.CharField(max_length=150, verbose_name='Слаг', **NULLABLE, default=slugify(header))
    text = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    date_of_creation = models.DateField(verbose_name='Дата создания', default=now)
    is_published = models.BooleanField(verbose_name='Было опубликовано', default=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    proprietor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.header}'

    class Meta:
        verbose_name = 'пост'  # Настройка для наименования одного объекта
        verbose_name_plural = 'посты'  # Настройка для наименования набора объектов
        ordering = ('header', 'date_of_creation')

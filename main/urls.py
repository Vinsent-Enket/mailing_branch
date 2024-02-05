from django.conf.urls.static import static

from config import settings
from django.urls import path
from django.views.decorators.cache import cache_page
from main.apps import MainConfig
from main.views import index

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='main_page'),
]

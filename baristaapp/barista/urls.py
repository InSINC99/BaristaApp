from django.urls import path
from .views import *

urlpatterns = [
    path('api/data/beans', get_beans, name='get_beans'),
    path('api/data/source', get_beans, name='get_source')
]

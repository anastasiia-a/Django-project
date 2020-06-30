from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url('see', views.index, name='index'),
    url('prod_id', views.id, name='id')
]
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'see/$', views.index, name='index'),
    url(r'^see/prod_id', views.prod_id, name='id')
]
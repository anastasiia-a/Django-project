from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^prod_id/', views.prod_id, name='id'),
    url(r'^search/', views.search),
    url(r'(?P<slug>[\w|/]+)$', views.products, name='products')
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^prod_id/', views.prod_id, name='id'),
    url(r'^search[\w|/]{0,}', views.search),
    url(r'(?P<slug>[\w|/]{0,})$', views.products, name='products')
]

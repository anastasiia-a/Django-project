from django.conf.urls import url
from django.utils.functional import curry
from django.views.defaults import server_error, page_not_found, permission_denied

from . import views

urlpatterns = [
    url(r'^prod_id/', views.prod_id, name='id'),
    url(r'^search/(?P<slug>[\w]+)', views.search),
    url(r'(?P<slug>[\w|/]{0,})$', views.products, name='products')
]

from django.conf.urls import url
from django.utils.functional import curry
from django.views.defaults import server_error, page_not_found, permission_denied

from . import views

handler404 = curry(server_error, template_name='catalog/404.html')
handler500 = curry(server_error, template_name='catalog/500.html')

urlpatterns = [
    url(r'^404$', handler404),
    url(r'^500$', handler500),
    url(r'^prod_id/', views.prod_id, name='id'),
    url(r'^search/(?P<slug>[\w]+)', views.search),
    url(r'(?P<slug>[\w|/]{0,})$', views.products, name='products')
]

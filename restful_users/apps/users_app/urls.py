from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^users$', views.index),
    url(r'^users/(?P<id>\d+)$', views.show),
    url(r'^users/new', views.new),
    url(r'^users/(?P<id>\d+)/edit$', views.edit),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy)
]
from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^(?P<id>[0-9]+)/join$', views.join),
    url(r'^(?P<id>[0-9]+)/drop$', views.drop),
    url(r'^(?P<id>[0-9]+)/edit$', views.edit),
    url(r'^(?P<id>[0-9]+)/delete$', views.delete),
    url(r'^(?P<id>[0-9]+)/confirm$', views.confirm),
    url(r'^(?P<id>[0-9]+)$', views.update),  
]
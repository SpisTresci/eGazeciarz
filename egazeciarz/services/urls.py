from django.conf.urls import patterns, url

from services import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'(?P<service_id>\d+)/', views.detail, name='detail'),
    url(r'^(?P<service_id>\d+)/save$', views.save, name='save'),
)

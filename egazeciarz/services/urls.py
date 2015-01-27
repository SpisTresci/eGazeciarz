from django.conf.urls import patterns, url

from services import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView, name='index'),
    url(r'^(?P<service_id>\d+)/([\w-]+)?$', views.DetailView, name='detail'),
    url(r'^(?P<service_id>\d+)/save$', views.save, name='save'),
)

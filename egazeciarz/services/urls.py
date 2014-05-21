from django.conf.urls import patterns, url

from services import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<service_id>\d+)/save$', views.save, name='save'),
)

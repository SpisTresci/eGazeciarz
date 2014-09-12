from django.conf.urls import patterns, url

from rank import views

urlpatterns = patterns(
    '',
    url(r'^$', views.Rank.as_view(), name='index'),
)

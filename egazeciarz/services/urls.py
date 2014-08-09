from django.conf.urls import patterns, url
from django.contrib.auth.views import password_change

from services import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^change-password/$', password_change, {'post_change_redirect': '/'}, name='change_password'),
    url(r'^user-panel/$', views.UserPanelView.as_view(), name='user_panel'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<service_id>\d+)/save$', views.save, name='save'),
)

from django.conf.urls import patterns, url

from services import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^user-panel/$', views.UserPanelView.as_view(), name='user_panel'),
    url(r'^password-change/$', views.ChangePasswordView.as_view(), name='change_password'),
    url(r'^email-change/$', views.ChangeEmailView.as_view(), name='change_email'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<service_id>\d+)/save$', views.save, name='save'),
)

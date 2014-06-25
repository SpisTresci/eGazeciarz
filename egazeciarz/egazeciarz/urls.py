from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('allauth.urls')),
    url(r'^services/', include('services.urls', namespace='services')),
)

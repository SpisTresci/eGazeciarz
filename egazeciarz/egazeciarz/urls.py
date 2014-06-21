from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^services/', include('services.urls', namespace='services')),
)

urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)


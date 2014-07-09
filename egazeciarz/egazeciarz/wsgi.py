"""
WSGI config for egazeciarz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from django.core.handlers.wsgi import WSGIHandler


class WSGIEnvironment(WSGIHandler):
    def __call__(self, environ, start_response):
        os.environ['DJANGO_SETTINGS_MODULE'] =\
            environ['DJANGO_SETTINGS_MODULE']
        return super(WSGIEnvironment, self).__call__(environ, start_response)

application = WSGIEnvironment()

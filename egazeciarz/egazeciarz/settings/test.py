from default import *
try:
    from local_settings import (
        EMAIL_HOST_USER as USER,
        EMAIL_HOST_PASSWORD as PASSWORD,
    )

except ImportError:
    print "Can't find local_settings.py"

DEBUG = True

# MailCatcher
if DEBUG:
    EMAIL_HOST = '127.0.0.1'
    EMAIL_HOST_USER = USER
    EMAIL_HOST_PASSWORD = PASSWORD
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'test.egazeciarz.pl',
]

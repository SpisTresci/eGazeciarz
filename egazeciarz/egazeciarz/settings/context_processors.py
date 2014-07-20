from django.conf import settings


def context_processor(request):
    return {
        'is_dev': settings.IS_DEV,
        'is_test': settings.IS_TEST,
        'is_staging': settings.IS_STAGING,
        'is_prod': settings.IS_PROD,
        'DEBUG': settings.DEBUG,
        'ENV': settings.ENV,
    }

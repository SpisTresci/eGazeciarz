from django.conf import settings


def context_processor(request):
    return {
        'is_dev': settings.IS_DEV,
        'is_staging': settings.IS_STAGING,
        'is_prod': settings.IS_PROD,
    }

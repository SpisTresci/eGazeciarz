from django.shortcuts import render

from services.models import Service

def index(request):
    services_list = Service.objects.all()
    context = { 'services_list': services_list }
    return render(request, 'services/index.html', context)

def detail(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        raise Http404
    return render(request, 'services/detail.html', {'service': service})


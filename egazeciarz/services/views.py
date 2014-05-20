from django.http import Http404
from django.shortcuts import render, get_object_or_404

from services.models import Service

def index(request):
    services_list = Service.objects.all()
    context = { 'services_list': services_list }
    return render(request, 'services/index.html', context)

def detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'services/detail.html', {'service': service})

def save(request, service_id):
    service = get_object_or_404(Service, id=service_id)

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic

from services.models import Service


class IndexView(generic.ListView):
    template_name = 'services/index.html'
    context_object_name = 'services_list'

    def get_queryset(self):
        return Service.objects.all()


class DetailView(generic.DetailView):
    template_name = 'services/detail.html'
    model = Service


def save(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if 'status' in request.POST:
        service.status = True
    else:
        service.status = False
    service.save()
    return HttpResponseRedirect(reverse('services:detail', args=service_id))

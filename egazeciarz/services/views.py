# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic

from services.models import Service


from django.shortcuts import render

context = {
    'sections': [
        {
            'name': 'Polskie',
            'services': [
                {
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'Newsweek Polska',
                },
                {
                    'cover': 'http://i.imgur.com/qn51KVR.png',
                    'title': u'Gazeta Wyborcza',
                },
                {
                    'cover': 'http://i.imgur.com/kfbAP6E.png',
                    'title': u'Niebezpiecznik.pl',
                },
                {
                    'cover': 'http://i.imgur.com/1N7wlti.png',
                    'title': u'Czytania na każdy dzień',
                },
                {
                    'cover': 'http://i.imgur.com/5IACxjT.png',
                    'title': u'eKundelek.pl',
                },
                {
                    'cover': 'http://i.imgur.com/1Pcdry3.png',
                    'title': u'Bash.org.pl',
                },
                {
                    'cover': 'http://i.imgur.com/4UG050N.png',
                    'title': u'Bankier.pl',
                },
                {
                    'cover': 'http://i.imgur.com/4hXCAjx.png',
                    'title': u'Gazeta Prawna',
                },
            ],
        },
        {
            'name': 'Angielskie',
            'services': [
                {
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'Newsweek',
                },
                {
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'New York Times',
                },
                {
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'Linux Weekly News',
                },
                {
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'Slashdot',
                },
            ],
        },
        {
            'name': 'Angielskie (UK)',
            'services': [],
        },
        {
            'name': 'Hiszpańskie',
            'services': [],
        },
        {
            'name': 'Niemieckie',
            'services': [],
        },
        {
            'name': 'Program TV',
            'services': [],
        },
        {
            'name': 'Inne',
            'services': [],
        },
    ],
}

# context zdefiniowany na potrzeby frontendu
# TODO: context powinien być generowany dynamicznie


def IndexView(request):
    return render(request, 'services/index.html', context)


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

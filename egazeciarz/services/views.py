# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic

from services.models import Service


from django.shortcuts import render

index_context = {


    'sections': [
        {
            'id': 1,
            'name': 'Polskie',
            'services': [
                {
                    'id': 1,
                    'cover': 'http://i.imgur.com/4hXCAjx.png',
                    'title': u'Gazeta Prawna',
                },
                {
                    'id': 2,
                    'cover': 'http://i.imgur.com/qn51KVR.png',
                    'title': u'Gazeta Wyborcza',
                },
                {
                    'id': 3,
                    'cover': 'http://i.imgur.com/kfbAP6E.png',
                    'title': u'Niebezpiecznik.pl',
                },
                {
                    'id': 4,
                    'cover': 'http://i.imgur.com/1N7wlti.png',
                    'title': u'Czytania na każdy dzień',
                },
                {
                    'id': 5,
                    'cover': 'http://i.imgur.com/5IACxjT.png',
                    'title': u'eKundelek.pl',
                },
                {
                    'id': 6,
                    'cover': 'http://i.imgur.com/1Pcdry3.png',
                    'title': u'Bash.org.pl',
                },
                {
                    'id': 7,
                    'cover': 'http://i.imgur.com/4UG050N.png',
                    'title': u'Bankier.pl',
                },
                {
                    'id': 8,
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'Newsweek Polska',
                },
            ],
        },
        {
            'id': 2,
            'name': 'Angielskie',
            'services': [
                {
                    'id': 9,
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'Newsweek',
                },
                {
                    'id': 10,
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'New York Times',
                },
                {
                    'id': 11,
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'Linux Weekly News',
                },
                {
                    'id': 12,
                    'cover': 'http://i.imgur.com/Ei4tfbo.png',
                    'title': u'Slashdot',
                },
            ],
        },
        {
            'id': 3,
            'name': 'Angielskie (UK)',
            'services': [],
        },
        {
            'id': 4,
            'name': 'Hiszpańskie',
            'services': [],
        },
        {
            'id': 5,
            'name': 'Niemieckie',
            'services': [],
        },
        {
            'id': 6,
            'name': 'Program TV',
            'services': [],
        },
        {
            'id': 7,
            'name': 'Inne',
            'services': [],
        },
    ],
}

# context zdefiniowany na potrzeby frontendu
# TODO: context powinien być generowany dynamicznie


def IndexView(request):
    return render(request, 'services/index.html', index_context)


# class DetailView(generic.DetailView):
#     template_name = 'services/detail.html'
#     model = Service

def DetailView(request, service_id):
    context = {
        'days_of_the_week': [
            (0, u"Poniedziałek"),
            (1, u"Wtorek"),
            (2, u"Środa"),
            (3, u"Czwartek"),
            (4, u"Piątek"),
            (5, u"Sobota"),
            (6, u"Niedziela"),
        ],
        'hours_per_day': range(24),

        'subscribed': [
            (3, 15),
            (5, 12),
            (2, 6),
            (2, 10),
        ],

        'id': 1,
        'name': u"Antyweb.pl",
        'section_id': 1,
        'description':
            u"Grzegorz Marczak opisuje wydarzenia w Polskim "
            u"i światowym internecie."
    }

    context.update(index_context)

    return render(request, 'services/detail.html', context)


def save(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if 'status' in request.POST:
        service.status = True
    else:
        service.status = False
    service.save()
    return HttpResponseRedirect(reverse('services:detail', args=service_id))

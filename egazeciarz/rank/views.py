from django.db.models.aggregates import Count
from django.views.generic.base import TemplateView
from services.models import Subscription


class Rank(TemplateView):

    template_name = 'rank.html'

    def get_context_data(self, **kwargs):
        context = super(Rank, self).get_context_data(**kwargs)

        context['subscriptions'] = Subscription.objects.annotate(
            count=Count('userssubs'),
        ).order_by(
            '-count'
        )

        return context
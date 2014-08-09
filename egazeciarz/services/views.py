from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_text
from django.views import generic
from django.views.generic.base import ContextMixin
from django.views.generic.edit import ModelFormMixin

from services.forms import ChangeUserEmailForm
from services.models import Service


#class MultipleFormsMixin(ContextMixin):
#    """
#    A mixin that provides a way to show and handle multiple forms on one page.
#    Usage:
#        form_classes (dict): should contain all used forms with keys clearly
#        describing form operation or purpose.
#        prefixes (dict): not required however recommended to explicitly mark
#        form fields membership.
#    """

#    form_classes = {}
#    prefixes = {}

#    def get_prefixes(self):
#        return self.prefixes

#    def get_form_classes(self):
#        return self.form_classes

#    def get_forms_kwargs(self):
#        forms_kwargs = {}
#        for form in self.form_classes.iterkeys():
#            forms_kwargs[form] = {
#                'prefix': self.get_prefixes()[form]
#            }
#            if self.request.method in ('POST', 'PUT'):
#                forms_kwargs[form].update({
#                    'data': self.request.POST,
#                    'files': self.request.FILES,
#                })
#        return forms_kwargs

#    def get_forms(self, form_classes):
#        forms_kwargs = self.get_forms_kwargs()
#        return {f[0]: f[1](**f[2]) for f in zip(form_classes.iterkeys(),
#                                                form_classes.itervalues(),
#                                                forms_kwargs.itervalues())}

#    def get_success_url(self):
#        if self.success_url:
#            url = force_text(self.success_url)
#        else:
#            raise ImproperlyConfigured(
#                'No URL to redirect to. Provide a success url.')
#        return url

#    def form_valid(self, form):
#        return HttpResponseRedirect(self.success_url)

#    def form_invalid(self, forms):
#        return self.render_to_response(self.get_context_data(**forms))

class IndexView(generic.ListView):
    template_name = 'services/index.html'
    context_object_name = 'services_list'

    def get_queryset(self):
        return Service.objects.all()


class DetailView(generic.DetailView):
    template_name = 'services/detail.html'
    model = Service


# http://stackoverflow.com/questions/15497693/django-can-class-based-views-accept-two-forms-at-a-time
class UserPanelView(generic.UpdateView):
    template_name = 'services/user_panel.html'
    form_class = PasswordChangeForm
    change_email_form_class = ChangeUserEmailForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        ctx = {}
        user = self.request.user
        ctx.setdefault('password_change_form', self.form_class(user=user, prefix='password_change'))
        ctx.setdefault('change_email_form', self.change_email_form_class(self.request.POST, prefix='change_email'))
        return self.render_to_response(self.get_context_data(**ctx))


    def get_context_data(self, **kwargs):
        ctx = super(UserPanelView, self).get_context_data(**kwargs)
        user = self.request.user
        ctx.setdefault('password_change_form', self.form_class(user=user, prefix='password_change'))
        ctx.setdefault('change_email_form', self.change_email_form_class(self.request.POST, prefix='change_email'))
        return ctx

    def get_object(self):
        return self.request.user

    def form_invalid(self, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'password_change_form' in request.POST:
            form_class = self.form_class
            form_name = 'password_change_form'
            form = form_class(user=self.object, data=request.POST, prefix='password_change')
        else:
            form_class = self.change_email_form_class
            form_name = 'change_email_form'
            form = form_class(data=request.POST, prefix='change_email')

        self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name: form})


def save(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if 'status' in request.POST:
        service.status = True
    else:
        service.status = False
    service.save()
    return HttpResponseRedirect(reverse('services:detail', args=service_id))

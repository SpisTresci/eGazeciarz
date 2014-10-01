from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.views import generic
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.template import RequestContext

from services.forms import ChangeUserEmailForm
from services.models import Service


class IndexView(generic.ListView):
    template_name = 'services/index.html'
    context_object_name = 'services_list'

    def get_queryset(self):
        return Service.objects.all()


class DetailView(generic.DetailView):
    template_name = 'services/detail.html'
    model = Service


# http://stackoverflow.com/questions/15497693/django-can-class-based-views-accept-two-forms-at-a-time
class UserPanelView(generic.TemplateView):
    template_name = 'profile/account_panel.html'
    form_class = PasswordChangeForm
    change_email_form_class = ChangeUserEmailForm
    success_url = reverse_lazy('home')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserPanelView, self).dispatch(*args, **kwargs)

    #def get(self, request, *args, **kwargs):
        #ctx = {}
        #user = self.request.user
        #ctx.setdefault('password_change_form',
        #               self.form_class(user=user, prefix='password_change'),
        #               )
        #ctx.setdefault('change_email_form',
        #               self.change_email_form_class(self.request.POST,
        #                                            prefix='change_email',
        #                                            ),
        #               )
        #return self.render_to_response(self.get_context_data(**))

    #def get_context_data(self, **kwargs):
    #    ctx = super(UserPanelView, self).get_context_data(**kwargs)
    #    user = self.request.user
    #    ctx.setdefault('password_change_form',
    #                   self.form_class(user=user, prefix='password_change')
    #                   )
    #    ctx.setdefault('change_email_form',
    #                   self.change_email_form_class(self.request.POST,
    #                                                prefix='change_email',
    #                                                ),
    #                   )
    #    return ctx


class ChangePasswordView(generic.UpdateView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('services:user_panel')
    template_name = 'includes/change_password.html'

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChangePasswordView, self).dispatch(*args, **kwargs)

    def get_object(self):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super(generic.edit.ModelFormMixin, self).get_form_kwargs()
        kwargs.update({'user': self.object})
        return kwargs

    def form_invalid(self, form):
        print 'form invalid'
        #return render_to_response(self.template_name,
        #                          self.get_context_data(form=form),
        #                          context_instance=RequestContext(self.request))
        return self.response_class(
            request=self.request,
            template='includes/change_password.html',
            context=self.get_context_data(form=form),
            **{'content_type': self.content_type}
        )

    def form_valid(self, form):
        print 'form valid'
        form.save()
        return self.response_class(
            request=self.request,
            template='includes/change_password.html',
            context=self.get_context_data(success=True),
            **{'content_type': self.content_type}
        )


class ChangeEmailView(generic.UpdateView):
    form_class = ChangeUserEmailForm
    success_url = reverse_lazy('services:user_panel')
    template_name = 'includes/change_email.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChangeEmailView, self).dispatch(*args, **kwargs)

    def get_object(self):
        return self.request.user

    def form_invalid(self, form):
        #return render_to_response()
        return self.response_class(
            request=self.request,
            template='includes/change_email.html',
            context=self.get_context_data(form=form),
            **{'content_type': self.content_type}
        )

    def form_valid(self, form):
        form.save()
        return self.response_class(
            request=self.request,
            template='includes/change_email.html',
            context=self.get_context_data(success=True),
            **{'content_type': self.content_type}
        )

def save(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if 'status' in request.POST:
        service.status = True
    else:
        service.status = False
    service.save()
    return HttpResponseRedirect(reverse('services:detail', args=service_id))

user_panel_view = UserPanelView.as_view()

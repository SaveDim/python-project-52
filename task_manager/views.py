from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('Task manager')}


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/user_create.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('home')
    success_message = _('You are logged in')
    extra_context = {
        'title': _('Login'),
        'button_text': _('Enter'),
    }

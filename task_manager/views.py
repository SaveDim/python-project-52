from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('index.html')


class UserLoginView(CreateView):
    form_class = UserCreationForm
    template_name = "user_login.html"
    success_url = _("index.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = _("Login user")
        return context

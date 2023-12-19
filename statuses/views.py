from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserCreateForm
from .models import TaskStatus


class StatusListView(ListView):
    model = TaskStatus
    template_name = "statuses/statuses.html"
    context_object_name = "users"
    extra_context = {"header": _("Users")}


class StatusCreateView(SuccessMessageMixin, CreateView):
    template_name = "users/user_create.html"
    model = TaskStatus
    form_class = UserCreateForm
    success_url = reverse_lazy("user_login")
    success_message = _("User created successfully!")
    extra_context = {"header": _("Create user"),
                     "button": _("Register")
                     }


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = TaskStatus
    template_name = "statuses/status_create.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("user_list")
    success_message = _("User updated successfully!")
    extra_context = {"header": _("Update user"),
                     "button": _("Update")
                     }


class StatusDeleteView(DeleteView):
    model = TaskStatus
    template_name = "users/user_delete.html"
    success_url = reverse_lazy("user_list")
    success_message = _("User deleted successfully!")
    extra_context = {"header": _("Delete user"),
                     "button": _("Yes, delete")
                     }

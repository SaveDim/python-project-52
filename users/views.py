from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from users.forms import UserCreateForm
from .models import TaskManagerUser


class UserListView(ListView):
    model = TaskManagerUser
    template_name = "users/user_list.html"
    context_object_name = "users"
    extra_context = {"header": _("Users")}


class UserCreateView(CreateView):
    template_name = "users/user_create.html"
    model = TaskManagerUser
    form_class = UserCreateForm
    success_url = reverse_lazy("user_login")
    success_message = _("User created successfully!")
    extra_context = {"header": _("Create user"),
                     "button": _("Register")
                     }


class UserUpdateView(UpdateView):
    model = TaskManagerUser
    template_name = "users/user_create.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("user_list")
    success_message = _("User updated successfully!")
    extra_context = {"header": _("Update user"),
                     "button": _("Update")
                     }


class UserDeleteView(DeleteView):
    model = TaskManagerUser
    template_name = "user_delete.html"
    success_url = _("user_list")

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserCreateForm
from .models import TaskManagerUser


class IndexView(ListView):
    template_name = "index.html"
    extra_context = {"header": _("Users")}

class UserListView(ListView):
    model = TaskManagerUser
    template_name = "users/user_list.html"
    context_object_name = "users"
    extra_context = {"header": _("Users")}


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "users/user_create.html"
    model = TaskManagerUser
    form_class = UserCreateForm
    success_url = reverse_lazy("user_login")
    success_message = _("User created successfully!")
    extra_context = {"header": _("Create user"),
                     "button": _("Register")
                     }


class UserUpdateView(SuccessMessageMixin, UpdateView):
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
    template_name = "users/user_delete.html"
    success_url = reverse_lazy("user_list")
    success_message = _("User deleted successfully!")
    extra_context = {"header": _("Delete user"),
                     "button": _("Yes, delete")
                     }

from django.contrib.auth.models import User
from django.urls import reverse_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    table_context = {
        'header': _("Users"),
        'ID': _("ID"),
        'username': _("username"),
        'full_name': _("full name"),
        'created_at': _("created at"),
    }


class UserCreateView(CreateView):
    model = User
    template_name = "user_create.html"
    fields = ["username", "password", "first_name", "last_name"]
    success_url = _("user_list")


class UserUpdateView(UpdateView):
    model = User
    template_name = "user_update.html"
    fields = ["username", "email", "password", "first_name", "last_name"]
    success_url = _("user_list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = _("user_list")

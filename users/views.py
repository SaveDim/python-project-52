from django.contrib.auth.forms import UserCreationForm
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
    form_class = UserCreationForm
    template_name = "users/user_create.html"
    success_url = _("login")  # В ДЕМО ПРОЕКТЕ ПЕРЕЗОД НА СТРАНИЦУ ЛОГИНА

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = _("Create user")
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = "user_update.html"
    fields = ["username", "email", "password", "first_name", "last_name"]
    success_url = _("user_list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = _("user_list")

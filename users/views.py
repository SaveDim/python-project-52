from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from users.forms import UserCreateForm


class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "users"
    extra_context = {"header": _("Users")}


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "users/user_create.html"
    success_url = _("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = _("Create user")
        return context

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('user_login')
        return render(request, 'users/user_create.html', {'form': form})


class UserUpdateView(UpdateView):
    model = User
    template_name = "user_update.html"
    fields = ["username", "email", "password", "first_name", "last_name"]
    success_url = _("user_list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = _("user_list")

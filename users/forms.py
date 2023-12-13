from django.contrib.auth import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinLengthValidator


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        password_min_len = 3
        #
        # first_name = forms.CharField(
        #     label=_('Name'),
        #     widget=forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': _('Name'),
        #         }
        #     )
        # )
        #
        # last_name = forms.CharField(
        #     label=_('Surname'),
        #     widget=forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': _('Surname'),
        #         }
        #     )
        # )
        #
        # username = forms.CharField(
        #     label=_('Username'),
        #     widget=forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': _('Username'),
        #             'title': _('Not an option')
        #         }
        #     )
        # )
        #
        # password1 = forms.CharField(
        #     validators=[
        #         MinLengthValidator(password_min_len,
        #                            _("Password is too short")),
        #     ],
        #     label=_('Password'),
        #     widget=forms.PasswordInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': _('Password'),
        #             'title': _('Password must contains at least 3 chars')
        #         }
        #     )
        # )
        # password2 = forms.CharField(
        #     label=_('Password confirmation'),
        #     validators=[
        #         MinLengthValidator(password_min_len,
        #                            _("Password is too short")),
        #     ],
        #     widget=forms.PasswordInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': _('Password confirmation'),
        #             'title': _('Please, type your password again'),
        #         }
        #     )
        # )

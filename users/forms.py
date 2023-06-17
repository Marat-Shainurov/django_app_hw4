from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from main.forms import FormStyleMixin
from users.models import User


class RegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ProfileForm(FormStyleMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

from django.contrib.auth.forms import UserCreationForm

from main.forms import FormStyleMixin
from users.models import User


class RegisterForm(FormStyleMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

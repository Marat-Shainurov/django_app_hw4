import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic

from users.forms import RegisterForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        if form.is_valid():
            verification_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            new_user.set_password(verification_password)
            new_user.save()
            send_mail(
                'email verification',
                f'Your password - {verification_password}.',
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']]
            )
        return super().form_valid(form)

import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
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

    def form_valid(self, form):
        self.object = form.save()
        if form.is_valid():
            code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            self.object.verification_code = code
            self.object.save()
            send_mail(
                'email verification',
                f'Your password - {code}',
                settings.EMAIL_HOST_USER,
                [self.object.email]
            )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:verify_email', kwargs={'email': self.object.email})


def verify_email(request, email):
    if request.method == 'POST':
        code_to_check = request.POST.get('verification_code')
        user = User.objects.get(email=email)
        if user.verification_code == code_to_check:
            user.is_email_verified = True
            user.save()
            return redirect(reverse('users:login'))
        else:
            raise ValidationError(f'You have used the wrong code!')
    else:
        return render(request, 'users/verify_email.html')


def restore_user(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        user = User.objects.get(email=email)
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        send_mail(
            'email verification',
            f'Your new password - {new_password}. Use it for logging in.',
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse('users:login'))
    else:
        return render(request, 'users/restore_password.html')

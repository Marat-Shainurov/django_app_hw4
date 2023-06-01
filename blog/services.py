from django.core.mail import send_mail
from django.conf import settings


def send_email_hundred_views():
    send_mail(
        'You articles are very popular!',
        'Congratulations! One of the blogs has been viewed 100 times!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER]
    )

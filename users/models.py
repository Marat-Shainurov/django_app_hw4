from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models.blogs import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='user_email')
    avatar = models.ImageField(upload_to='avatar/', verbose_name='user_avatar', **NULLABLE)
    phone = models.CharField(max_length=40, verbose_name='user_phone', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='user_country', **NULLABLE)
    verification_code = models.CharField(verbose_name='email_verification_code', **NULLABLE)
    is_email_verified = models.BooleanField(verbose_name='is_email_verified', default=False, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

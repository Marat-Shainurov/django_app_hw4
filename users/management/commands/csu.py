from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User(
            email='m_shainurov@mail.ru',
            first_name='Marat',
            last_name='Shainurov',
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        user.set_password('123')
        user.save()

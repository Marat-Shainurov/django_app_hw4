# Generated by Django 4.2.1 on 2023-06-14 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_version_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='is_actual',
        ),
    ]

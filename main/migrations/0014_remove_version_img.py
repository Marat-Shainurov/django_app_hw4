# Generated by Django 4.2.1 on 2023-06-13 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_version_delete_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='img',
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='product_img'),
        ),
    ]

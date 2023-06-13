# Generated by Django 4.2.1 on 2023-06-13 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_version_is_actual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='main.product', verbose_name='product_name'),
        ),
    ]

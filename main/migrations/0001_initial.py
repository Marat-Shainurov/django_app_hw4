# Generated by Django 4.2.1 on 2023-05-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='prod_id')),
                ('name', models.CharField(max_length=100, verbose_name='prod_name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='prod_descr')),
                ('price', models.IntegerField(verbose_name='prod_price')),
                ('stock', models.IntegerField(verbose_name='prod_stock')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-10 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0003_products_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]

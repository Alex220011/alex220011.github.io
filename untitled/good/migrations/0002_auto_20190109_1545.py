# Generated by Django 2.1.5 on 2019-01-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='visit',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0007_auto_20190207_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='store',
        ),
        migrations.AddField(
            model_name='store',
            name='por',
            field=models.ManyToManyField(to='good.products'),
        ),
    ]
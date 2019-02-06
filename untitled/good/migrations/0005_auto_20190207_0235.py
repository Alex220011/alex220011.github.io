# Generated by Django 2.1.5 on 2019-02-06 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0004_products_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='store',
        ),
        migrations.AddField(
            model_name='store',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='good.products', verbose_name='Магазин'),
        ),
    ]

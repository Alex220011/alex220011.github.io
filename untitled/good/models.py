from django.db import models


class NameModel(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Store(NameModel):
    description = models.TextField(verbose_name='Описание', default='')

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'


class products(NameModel):
    description = models.TextField(verbose_name='Описание продукта', default='')
    store = models.ForeignKey(verbose_name='Магазин', to=Store,null=True, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена', default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

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


class Client(NameModel):
    description = models.TextField(verbose_name='Описание', default='')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Visit(NameModel):
    arrived = models.DateTimeField(verbose_name='Прибыл', null=True, auto_now_add=True)
    client = models.ForeignKey(verbose_name='Клиент', to=Client, on_delete=models.CASCADE)
    store = models.ForeignKey(verbose_name='Торговая точка', to=Store, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'

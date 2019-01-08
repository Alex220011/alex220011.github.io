from django.db import models

# Create your models here.


class Name(models.Model):
    name = models.CharField(verbose_name='Проверка гит хаба', max_length=30)

    class Meta:
        verbose_name = 'Пиццу'
        verbose_name_plural = 'Пиццы'

    def __str__(self):
        return self.name

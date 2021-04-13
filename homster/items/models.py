from django.db import models


class ItemName(models.Model):
    class Meta:
        verbose_name = 'Sterownik'
        verbose_name_plural = '1 Sterowniki'
        ordering = ['name']  # Sort in asc order

    name = models.CharField(max_length=16, verbose_name='Nazwa sterownika')
    description = models.CharField(max_length=64, verbose_name='Opis')
    num_pin = models.PositiveSmallIntegerField(verbose_name='Ilość pinów IO')

    def __str__(self):
        return f'{self.name} - {self.description}'

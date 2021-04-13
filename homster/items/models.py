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


class BussNameType(models.Model):
    class Meta:
        verbose_name = 'Magistrala'
        verbose_name_plural = '2 Magistrale'
        ordering = ['items_name__name', 'name']

    items_name = models.ForeignKey(ItemName, on_delete=models.CASCADE, verbose_name='Urządzenie')
    name = models.CharField(max_length=16, verbose_name='Magistrala')
    description = models.CharField(max_length=48, verbose_name='Opis')
    buss_adr = models.CharField(max_length=8, default=None, null=True, verbose_name='Adres komunikacji')

    def __str__(self):
        return f'{self.items_name.name} | {self.name} | {self.description}'

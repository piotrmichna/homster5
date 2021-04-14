from django.db import models


class CfgType(models.Model):
    class Meta:
        verbose_name = 'Typ komendy'
        verbose_name_plural = 'Typy komend'
        ordering = ['name']

    name = models.CharField(max_length=8, verbose_name="Komenda")
    description = models.CharField(max_length=64, null=True, verbose_name='Opis polecenia')

    def __str__(self):
        return f'{self.name} ({self.description})'


class CfgCommand(models.Model):
    class Meta:
        verbose_name = 'Konfiguracja'
        verbose_name_plural = 'Konfiguracja - komendy'
        ordering = ['name']

    type = models.ForeignKey(CfgType, on_delete=models.CASCADE, verbose_name='Typ komendy')
    name = models.CharField(max_length=16, verbose_name='Komenda')
    description = models.CharField(max_length=64, null=True, verbose_name='Opis polecenia')
    value = models.CharField(max_length=16, verbose_name='Wartość')

from django.db import models


class CfgType(models.Model):
    class Meta:
        verbose_name = 'Typ komendy'
        verbose_name_plural = 'Konfiguracja - typy komend'
        ordering = ['name']

    description = models.CharField(max_length=64, null=True, verbose_name='Opis typu polecenia')
    name = models.CharField(max_length=16, verbose_name="Nazwa typu polecenia")

    def __str__(self):
        return f'{self.description} ({self.name})'


class CfgCommand(models.Model):
    class Meta:
        verbose_name = 'Konfiguracja'
        verbose_name_plural = 'Konfiguracja - komendy'
        ordering = ['type__description', 'name']

    description = models.CharField(max_length=64, null=True, verbose_name='Opis polecenia')
    type = models.ForeignKey(CfgType, on_delete=models.CASCADE, verbose_name='Typ komendy')
    name = models.CharField(max_length=16, verbose_name='Komenda')
    value = models.CharField(max_length=16, verbose_name='Wartość')

    def __str__(self):
        return f'{self.type.description} - {self.description} ({self.value})'

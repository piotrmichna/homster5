from django.db import models


class ProgName(models.Model):
    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = '5 Programy'
        ordering = ['active', 'name']

    name = models.CharField(max_length=32, verbose_name="Nazwa programu")
    description = models.CharField(max_length=48, null=True, verbose_name='Opis programu')
    active = models.BooleanField(default=True, verbose_name='Aktywny')

    def __str__(self):
        if self.active:
            return f'{self.name} - {self.description} | (Aktywny)'
        else:
            return f'{self.name} - {self.description} | (Wyłączony)'

from django.db import models


class WeatherDayly(models.Model):
    class Meta:
        verbose_name = 'Pogoda kilkudniowa'
        verbose_name_plural = 'Pogoda kilkudniowa'
        ordering = ['time_m']

    time_m = models.DateTimeField(verbose_name='Data i czas pomiaru')
    temp_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Temperatura')
    pres_m = models.PositiveSmallIntegerField(verbose_name='Ciśnienie atmosferyczne')
    humi_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Wilgotność powietrza')
    sunl_m = models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')

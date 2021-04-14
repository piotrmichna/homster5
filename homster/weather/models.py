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
    ligh_m = models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')


class WeatherLong(models.Model):
    class Meta:
        verbose_name = 'Pogoda'
        verbose_name_plural = 'Pogoda'
        ordering = ['time_m']

    temp_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Temperatura')
    pres_m = models.PositiveSmallIntegerField(verbose_name='Ciśnienie atmosferyczne')
    humi_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Wilgotność powietrza')
    ligh_m = models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')

    time_day_start = models.TimeField(verbose_name='Czas rozpoczęcia dnia')
    time_day_stop = models.TimeField(verbose_name='Czas zakończenia dnia')

    temp_day_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Temperatura')
    pres_day_m = models.PositiveSmallIntegerField(verbose_name='Ciśnienie atmosferyczne')
    humi_day_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Wilgotność powietrza')
    ligh_day_m = models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')
    temp_night_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Temperatura')
    pres_night_m = models.PositiveSmallIntegerField(verbose_name='Ciśnienie atmosferyczne')
    humi_night_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Wilgotność powietrza')
    ligh_day_m = models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')

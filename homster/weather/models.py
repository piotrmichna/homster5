from django.db import models


class WeatherDaily(models.Model):
    class Meta:
        verbose_name = 'Pogoda kilkudniowa'
        verbose_name_plural = 'Pogoda kilkudniowa'
        ordering = ['time_m']

    time_m = models.DateTimeField(verbose_name='Data i czas pomiaru')
    temp_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Temperatura')
    pres_m = models.PositiveSmallIntegerField(verbose_name='Ciśnienie atmosferyczne')
    humi_m = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Wilgotność powietrza')
    ligh_m = models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')

    def __str__(self):
        return f'{self.time_m.strftime("%Y-%m-%d")} {self.time_m.strftime("%H:%M:%S")} => ({self.temp_m}°C | {self.pres_m}hPa | {self.humi_m}% | {self.ligh_m}lx)'


class WeatherLong(models.Model):
    class Meta:
        verbose_name = 'Pogoda - średnia dzienna'
        verbose_name_plural = 'Pogoda - średnie dzienne'
        ordering = ['date_m']

    date_m = models.DateField(verbose_name='Data pomiarów')
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
    ligh_night_m = models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')

    def __str__(self):
        return f'{self.date_m} ({self.temp_m}°C | {self.pres_m}hPa | {self.humi_m}% | {self.ligh_m}lx)'


class WeatherWeek(models.Model):
    class Meta:
        verbose_name = 'Pogoda - średnia tygodniowa'
        verbose_name_plural = 'Pogoda - średnie tygodniowe'
        ordering = ['date_m']

    date_m = models.DateField(verbose_name='Data pomiarów')
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
    ligh_night_m = models.PositiveSmallIntegerField(verbose_name='Nasłonecznienie')

    def __str__(self):
        return f'{self.date_m} ({self.temp_m}°C | {self.pres_m}hPa | {self.humi_m}% | {self.ligh_m}lx)'

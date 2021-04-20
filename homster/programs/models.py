from django.db import models

from items.models import GpioPinCfg


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


class ProgStartTime(models.Model):
    class Meta:
        verbose_name = 'Program - pory uruchomień'
        verbose_name_plural = '7 Programy - pory uruchomień'
        ordering = ['start_time', 'name']

    name = models.CharField(max_length=16, verbose_name="Nazwa startu")
    description = models.CharField(max_length=32, null=True, verbose_name='Opis startu')
    day_delay = models.PositiveSmallIntegerField(default=0, verbose_name='Ilość dni przerwy')
    start_time = models.TimeField(default='07:00:00', verbose_name='Godzina uruchomienia')
    active = models.BooleanField(default=True, verbose_name='Aktywny')

    prog = models.ForeignKey(ProgName, related_name='progstarts', on_delete=models.CASCADE, verbose_name='Dla programu')

    def __str__(self):
        if self.active:
            return f'{self.name} - {self.description} | (Aktywny)'
        else:
            return f'{self.name} - {self.description} | (Wyłączony)'


def int_tim_str(n):
    try:
        n = int(n)
    except ValueError:
        n = 1
    if n < 10:
        return f'0{n}'
    else:
        return str(n)


def sec_to_tim(sec):
    try:
        s = int(sec)
    except ValueError:
        s = 1
    m = 0
    h = 0
    if sec > 59:
        m = sec // 60
        s = sec - m * 60
        if m > 59:
            h = m // 60
            m = m - h * 60

    return int_tim_str(h) + ":" + int_tim_str(m) + ":" + int_tim_str(s)


class ProgPinCfg(models.Model):
    class Meta:
        verbose_name = "Program - urządzenia"
        verbose_name_plural = '6 Programy - urządzenia'
        ordering = ['lp']

    prog = models.ForeignKey(ProgName, related_name='progpin', on_delete=models.CASCADE, verbose_name='Dla programu')
    pin_cfg = models.ForeignKey(GpioPinCfg, related_name='gpiopins', on_delete=models.CASCADE,
                                verbose_name='Pin sterujący')
    lp = models.PositiveSmallIntegerField(default=0, verbose_name='Kolejność')
    duration_sec = models.PositiveSmallIntegerField(default=1, verbose_name='Czas trwania [s]')

    class Meta:
        unique_together = ['prog', 'pin_cfg', 'lp']
        ordering = ['prog', 'lp']

    def __str__(self):
        dur_time = sec_to_tim(self.duration_sec)
        return f'{self.pin_cfg.name} - {dur_time} | (Aktywny)'

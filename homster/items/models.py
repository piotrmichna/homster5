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


class BussPinType(models.Model):
    class Meta:
        verbose_name = 'Magistrala - pin'
        verbose_name_plural = '3 Magistrale - piny'
        ordering = ['items_name__name', 'pin_board']

    items_name = models.ForeignKey(ItemName, on_delete=models.CASCADE, verbose_name='Urządzenie')
    buss_name = models.ForeignKey(BussNameType, on_delete=models.CASCADE, verbose_name='Magistrala')
    name = models.CharField(max_length=16, verbose_name='Nazwa pinu')
    description = models.CharField(max_length=48, verbose_name='Opis pinu')
    pin_board = models.PositiveSmallIntegerField(verbose_name='Numer pinu')

    def __str__(self):
        return f'{self.items_name.name} | [{self.pin_board}] | {self.buss_name.name} - {self.name}'


class GpioPinCfg(models.Model):
    class Meta:
        verbose_name = 'Konfiguracja modułu'
        verbose_name_plural = '4 Konfiguracja modułów'
        ordering = ['name']

    buss_pin = models.ForeignKey(BussPinType, related_name='gpio_pins', on_delete=models.CASCADE, verbose_name='IO sterownika')
    name = models.CharField(max_length=16, null=True, verbose_name='Nazwa modułu')
    description = models.CharField(max_length=48, null=True, verbose_name='Opis modułu')
    pin_board = models.PositiveSmallIntegerField(null=False, verbose_name='Numer pinu')
    dir_out = models.BooleanField(null=False, default=True, verbose_name='Kierunek wyjściowy')
    val = models.PositiveSmallIntegerField(null=True, verbose_name='Stan aktualny')
    val_default = models.PositiveSmallIntegerField(null=True, verbose_name='Wartość domyślna')

    def __str__(self):
        if self.dir_out:
            return f'{self.name} | [{self.pin_board}]out | {self.description}'
        else:
            return f'{self.name} ({self.pin_board})in  | {self.description}'

from django.core.management import BaseCommand
from items.management.commands_data.items_data import (ITEMS_NAME, BUSS_NAME, BUSS_PIN, GPIO_PIN_DATA)
from items.models import (ItemName, BussNameType, BussPinType, GpioPinCfg)


def insert_items_name():
    for n, d, np in ITEMS_NAME:
        ItemName.objects.create(name=n, description=d, num_pin=np)


def insert_buss_name():
    items_names = ItemName.objects.values_list('name', flat=True)
    for item_name in items_names:
        item_n = ItemName.objects.get(name=item_name)
        for i, n, d in BUSS_NAME:
            if i == item_n.name:
                BussNameType.objects.create(items_name=item_n, name=n, description=d)


def insert_buss_pin():
    items_names = ItemName.objects.values_list('name', flat=True)
    for item_name in items_names:
        item_n = ItemName.objects.get(name=item_name)
        for i, n, d, p, b in BUSS_PIN:
            if i == item_n.name:
                buss = BussNameType.objects.get(name=b)
                BussPinType.objects.create(items_name=item_n, buss_name=buss, name=n,
                                           description=d, pin_board=p)


def insert_gpio_pin():
    for bn, n, d, p, do, v, vd in GPIO_PIN_DATA:
        buss_p = BussPinType.objects.get(name=bn)
        GpioPinCfg.objects.create(buss_pin=buss_p, name=n, description=d, pin_board=p, dir_out=do,
                                  val=v, val_default=vd)


class Command(BaseCommand):
    help = 'Wstawienie danych urządzeń do bazy.'

    def handle(self, *args, **options):
        insert_items_name()
        insert_buss_name()
        insert_buss_pin()
        insert_gpio_pin()
        print('Pomyślnie dodano dane urządzeń do bazy.')
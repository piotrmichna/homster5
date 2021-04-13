# from django.core.management import BaseCommand
from items.management.commands_data.items_data import (ITEMS_NAME, BUSS_NAME)
from items.models import (ItemName, BussNameType)


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

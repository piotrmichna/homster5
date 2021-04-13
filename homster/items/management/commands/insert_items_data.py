# from django.core.management import BaseCommand
from items.management.commands_data.items_data import (ITEMS_NAME, BUSS_NAME)
from items.models import (ItemName, BussNameType)


def insert_items_name():
    for n, d, np in ITEMS_NAME:
        ItemName.objects.create(name=n, description=d, num_pin=np)

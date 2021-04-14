from django.core.management import BaseCommand

from items.models import GpioPinCfg
from programs.management.commands_data.programs_data import (PROG_NAME_DATA, PROG_START_DATA, PROG_PIN_DATA)
from programs.models import (ProgName, ProgStartTime, ProgPinCfg)


def delete_prog_all():
    ProgPinCfg.objects.all().delete()
    ProgStartTime.objects.all().delete()
    ProgName.objects.all().delete()


def insert_prog_name():
    for n, d, a in PROG_NAME_DATA:
        ProgName.objects.create(name=n, description=d, active=a)


def insert_prog_start():
    for n, d, dd, st, a, p in PROG_START_DATA:
        pr = ProgName.objects.get(name=p)
        ProgStartTime.objects.create(name=n, description=d, day_delay=dd, start_time=st, active=a, prog=pr)


def insert_prog_pin():
    for prn, pn, lp, t in PROG_PIN_DATA:
        pr = ProgName.objects.get(name=prn)
        pin = GpioPinCfg.objects.get(name=pn)
        ProgPinCfg.objects.create(prog=pr, pin_cfg=pin, lp=lp, duration_sec=t)
        # ['Test', 'Sekcja 1', 1, 2],


class Command(BaseCommand):
    help = 'Wstawienie danych programów do bazy.'

    def handle(self, *args, **options):
        delete_prog_all()
        insert_prog_name()
        insert_prog_start()
        insert_prog_pin()
        print('Pomyślnie dodano dane programów do bazy.')

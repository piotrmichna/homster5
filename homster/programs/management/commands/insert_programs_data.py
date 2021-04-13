from programs.management.commands_data.programs_data import PROG_NAME_DATA, PROG_START_DATA
from programs.models import ProgName, ProgStartTime


def insert_prog_name():
    for n, d, a in PROG_NAME_DATA:
        ProgName.objects.create(name=n, description=d, active=a)


def insert_prog_start():
    for n, d, dd, st, a, p in PROG_START_DATA:
        pr = ProgName.objects.get(name=p)
        ProgStartTime.objects.create(name=n, description=d, day_delay=dd, start_time=st, active=a, prog=pr)

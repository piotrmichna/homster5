from programs.management.commands_data.programs_data import PROG_NAME_DATA
from programs.models import ProgName


def insert_prog_name():
    for n, d, a in PROG_NAME_DATA:
        ProgName.objects.create(name=n, description=d, active=a)

from django.core.management import BaseCommand

from config.management.commands_data.config_data import CFG_TYPE_DATA, CFG_COMMAND_DATA
from config.models import CfgType, CfgCommand


def delete_cfg_all():
    CfgCommand.objects.all().delete()
    CfgType.objects.all().delete()


def insert_cfg_type():
    for n, d in CFG_TYPE_DATA:
        CfgType.objects.create(name=n, description=d)


def insert_cfg_command():
    for tn, n, d, v in CFG_COMMAND_DATA:
        tp = CfgType.objects.get(name=tn)
        CfgCommand.objects.create(type=tp, name=n, description=d, value=v)


class Command(BaseCommand):
    help = 'Wstawienie danych konfiguracji do bazy.'

    def handle(self, *args, **options):
        delete_cfg_all()
        insert_cfg_type()
        insert_cfg_command()
        print('Pomyślnie dodano polecenia konfiguracji do bazy.')

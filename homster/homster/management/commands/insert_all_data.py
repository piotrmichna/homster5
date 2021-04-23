from django.core.management import BaseCommand

from config.management.commands.insert_config_data import insert_command_all, delete_cfg_all
from items.management.commands.insert_items_data import insert_items_all, delete_items_all
from programs.management.commands.insert_programs_data import insert_programs_all, delete_prog_all


class Command(BaseCommand):
    help = 'Wstawienie testowych danych do bazy.'

    def handle(self, *args, **options):
        delete_prog_all()
        delete_items_all()
        delete_cfg_all()

        insert_items_all()
        insert_programs_all()
        insert_command_all()

        print('Pomyślnie dodano polecenia konfiguracji do bazy.')

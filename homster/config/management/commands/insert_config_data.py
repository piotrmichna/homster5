from config.management.commands_data.config_data import CFG_TYPE_DATA
from config.models import CfgType


def insert_cfg_type():
    for n, d in CFG_TYPE_DATA:
        CfgType.objects.create(name=n, description=d)


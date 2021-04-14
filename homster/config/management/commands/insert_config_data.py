from config.management.commands_data.config_data import CFG_TYPE_DATA
from config.models import CfgType


def insert_cfg_type():
    for n, d in CFG_TYPE_DATA:
        CfgType.objects.create(name=n, description=d)


def insert_cfg_command():
    for tn, n, d, v in CFG_COMMAND_DATA:
        tp = CfgType.objects.get(name=tn)
        CfgCommand.objects.create(type=tp, name=n, description=d, value=v)


from django.contrib import admin

from config.models import CfgCommand, CfgType

admin.site.register(CfgType)
admin.site.register(CfgCommand)

from django.contrib import admin

from programs.models import ProgName, ProgStartTime, ProgPinCfg

admin.site.register(ProgName)
admin.site.register(ProgStartTime)
admin.site.register(ProgPinCfg)

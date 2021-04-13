from django.contrib import admin

from items.models import (ItemName, BussNameType, BussPinType, GpioPinCfg)

admin.site.register(ItemName)
admin.site.register(BussNameType)
admin.site.register(BussPinType)
admin.site.register(GpioPinCfg)

from django.contrib import admin

from weather.models import WeatherDaily, WeatherWeek, WeatherLong

admin.site.register(WeatherDaily)
admin.site.register(WeatherWeek)
admin.site.register(WeatherLong)

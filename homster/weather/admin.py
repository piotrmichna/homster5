from django.contrib import admin

from weather.models import WeatherDaily, WeatherWeek

admin.site.register(WeatherDaily)
admin.site.register(WeatherWeek)

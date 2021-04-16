from rest_framework import serializers

from config.models import CfgCommand
from weather.models import (WeatherDaily, WeatherLong, WeatherWeek)


class WeatherDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDaily
        fields = (
            'id',
            'time_m',
            'temp_m',
            'pres_m',
            'humi_m',
            'ligh_m',
        )


class WeatherLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherLong
        fields = (
            'date_m',
            'temp_m',
            'pres_m',
            'humi_m',
            'ligh_m',
            'time_day_start',
            'time_day_stop',
            'temp_day_m',
            'pres_day_m',
            'humi_day_m',
            'ligh_day_m',
            'temp_night_m',
            'pres_night_m',
            'humi_night_m',
            'ligh_night_m',
        )


class WeatherWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherWeek
        fields = (
            'date_m',
            'temp_m',
            'pres_m',
            'humi_m',
            'ligh_m',
            'time_day_start',
            'time_day_stop',
            'temp_day_m',
            'pres_day_m',
            'humi_day_m',
            'ligh_day_m',
            'temp_night_m',
            'pres_night_m',
            'humi_night_m',
            'ligh_night_m',
        )


class CfgWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CfgCommand
        fields = (
            'id',
            'description',
            'name',
            'value',
        )

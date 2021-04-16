from rest_framework import serializers

from weather.models import WeatherDaily


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

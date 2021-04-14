from rest_framework import viewsets

from rest.serializers import WeatherDailySerializer
from weather.models import WeatherDayly


class WeatherDailyViewSet(viewsets):
    serializer_class = WeatherDailySerializer
    queryset = WeatherDayly.objects.all()

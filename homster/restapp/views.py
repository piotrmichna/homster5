from rest_framework import viewsets

from restapp.serializers import (WeatherDailySerializer, WeatherLongSerializer, WeatherWeekSerializer)
from weather.models import (WeatherDaily, WeatherWeek)


class WeatherDailyViewSet(viewsets.ModelViewSet):
    serializer_class = WeatherDailySerializer
    queryset = WeatherDaily.objects.all()


class WeatherLongViewSet(viewsets.ModelViewSet):
    serializer_class = WeatherLongSerializer
    queryset = WeatherDaily.objects.all()


class WeatherWeekViewSet(viewsets.ModelViewSet):
    serializer_class = WeatherWeekSerializer
    queryset = WeatherWeek.objects.all()

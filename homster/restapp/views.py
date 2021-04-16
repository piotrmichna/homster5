from rest_framework import viewsets

from config.models import CfgCommand
from restapp.serializers import (WeatherDailySerializer, WeatherLongSerializer, WeatherWeekSerializer,
                                 CfgWeatherSerializer)
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


class CfgWeatherViewSet(viewsets.ModelViewSet):
    serializer_class = CfgWeatherSerializer
    queryset = CfgCommand.objects.filter(type__name='wthr')


class CfgSystemViewSet(viewsets.ModelViewSet):
    serializer_class = CfgWeatherSerializer
    queryset = CfgCommand.objects.filter(type__name='syst')


class CfgProgramViewSet(viewsets.ModelViewSet):
    serializer_class = CfgWeatherSerializer
    queryset = CfgCommand.objects.filter(type__name='prog')

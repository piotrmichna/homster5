from rest_framework import viewsets

from config.models import CfgCommand
from programs.models import ProgName, ProgPinCfg
from restapp.serializers import (WeatherDailySerializer, WeatherLongSerializer, WeatherWeekSerializer,
                                 CfgWeatherSerializer, ProgramsCfgSerializer, ProgPinCfgSerializer)
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


class ProgramsCfgViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramsCfgSerializer
    queryset = ProgName.objects.all().order_by('name')


class ProgPinCfgViewSet(viewsets.ModelViewSet):
    serializer_class = ProgPinCfgSerializer
    queryset = ProgPinCfg.objects.all().order_by('lp')

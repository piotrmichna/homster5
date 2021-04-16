from rest_framework import viewsets

from restapp.serializers import WeatherDailySerializer, WeatherLongSerializer
from weather.models import WeatherDaily


class WeatherDailyViewSet(viewsets.ModelViewSet):
    serializer_class = WeatherDailySerializer
    queryset = WeatherDaily.objects.all()


class WeatherLongViewSet(viewsets.ModelViewSet):
    serializer_class = WeatherLongSerializer
    queryset = WeatherDaily.objects.all()

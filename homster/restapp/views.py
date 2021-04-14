from rest_framework import viewsets

from restapp.serializers import WeatherDailySerializer
from weather.models import WeatherDaily


class WeatherDailyViewSet(viewsets.ModelViewSet):
    serializer_class = WeatherDailySerializer
    queryset = WeatherDaily.objects.all()

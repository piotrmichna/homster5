from django.shortcuts import render
from django.views import View

from weather.models import WeatherDaily


class WeatherChartsView(View):
    def get(self, request):
        queryset = WeatherDaily.objects.all()
        return render(request, 'plot.html', {'ctx': queryset})

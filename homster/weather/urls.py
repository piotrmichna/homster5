from django.urls import path

from weather.views import WeatherChartsView

urlpatterns = [
    path('', WeatherChartsView.as_view(), name='weather'),
]
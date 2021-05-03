from django.urls import path

from weather.views import WeatherChartsView, WeatherCreateDayView

urlpatterns = [
    path('', WeatherChartsView.as_view(), name='weather'),
    path('data/', WeatherCreateDayView.as_view(), name='weather'),
]
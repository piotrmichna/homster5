from django.urls import path

from weather.views import WeatherChartsView, WeatherCreateDayView

urlpatterns = [
    path('', WeatherChartsView.as_view(), name='weather'),
    path('data/<int:yy>/<int:mn>/<int:dy>/', WeatherCreateDayView.as_view(), name='weather-stats'),
]
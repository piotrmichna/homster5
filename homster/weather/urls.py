from django.urls import path

from weather.views import WeatherChartsView, WeatherCreateDayView, WeatherChartsDayView

urlpatterns = [
    path('', WeatherChartsView.as_view(), name='weather'),
    path('day/', WeatherChartsDayView.as_view(), name='weather-day'),
    path('data/<int:yy>/<int:mn>/<int:dy>/', WeatherCreateDayView.as_view(), name='weather-stats'),
]
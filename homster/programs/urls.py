from django.urls import path

from programs.views import ProgramslView
from weather.views import WeatherChartsView

urlpatterns = [
    path('', ProgramslView.as_view(), name='programs'),
]
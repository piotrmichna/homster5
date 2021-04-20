from rest_framework.routers import SimpleRouter

from restapp.views import (WeatherDailyViewSet, WeatherLongViewSet, WeatherWeekViewSet, CfgWeatherViewSet,
                           CfgSystemViewSet, CfgProgramViewSet, ProgramsCfgViewSet)

router = SimpleRouter()

router.register('weather/daily', WeatherDailyViewSet, basename='weather-daily')
router.register('weather/long', WeatherLongViewSet, basename='weather-long')
router.register('weather/week', WeatherWeekViewSet, basename='weather-week')
router.register('cfg/weather', CfgWeatherViewSet, basename='cfg-weather')
router.register('cfg/system', CfgSystemViewSet, basename='cfg-system')
router.register('cfg/program', CfgProgramViewSet, basename='cfg-program')
router.register('cfg/prog_name', ProgramsCfgViewSet, basename='cfg-prog_name')

urlpatterns = router.urls

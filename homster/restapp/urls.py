from rest_framework.routers import SimpleRouter

from restapp.views import (WeatherDailyViewSet, WeatherLongViewSet)

router = SimpleRouter()

router.register('weather/daily', WeatherDailyViewSet, basename='weather-daily')
router.register('weather/long', WeatherLongViewSet, basename='weather-long')

urlpatterns = router.urls

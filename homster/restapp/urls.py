from rest_framework.routers import SimpleRouter

from restapp.views import WeatherDailyViewSet

router = SimpleRouter()

router.register('weather/daily', WeatherDailyViewSet, basename='weather-daily')

urlpatterns = router.urls

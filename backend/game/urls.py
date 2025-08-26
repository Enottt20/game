from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from base.views import CsvLoaderViewSet, PlayerLevelViewSet


router = routers.DefaultRouter()
router.register('CSV_loader', CsvLoaderViewSet, 'CSV_loader')
router.register(
    'player_level_prize', PlayerLevelViewSet, 'player_level_prize'
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

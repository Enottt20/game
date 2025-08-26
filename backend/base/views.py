from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import PlayerLevel
from .serializers import LoaderPrizeSerializer, PlayerLevelSerializer
from .utils import loading_to_csv


class CsvLoaderViewSet(ReadOnlyModelViewSet):
    """Вьюсет выгрузки данных в CSV-файл."""

    queryset = PlayerLevel.objects.all()
    serializer_class = LoaderPrizeSerializer

    @action(detail=False)
    def loading_from_db(self, request):
        """Функция выгрузки данных в CSV-файл."""

        if request.method == 'GET':
            return loading_to_csv(request)


class PlayerLevelViewSet(ModelViewSet):
    """Вьюсет уровня игрока."""

    queryset = PlayerLevel.objects.all()
    serializer_class = PlayerLevelSerializer

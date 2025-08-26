import csv
from django.http import HttpResponse
from io import StringIO

from base.models import LevelPrize, PlayerLevel


def loading_to_csv(request):
    """Функция выгрузки данных в csv-файл."""

    fieldnames = ['Player_id', 'Level_title', 'Is_completed', 'Prize']
    csv_buffer = StringIO()
    writer = csv.DictWriter(
        csv_buffer, fieldnames=fieldnames, dialect='excel', delimiter=','
    )
    writer.writeheader()
    # Либо, непосредственная запиь в файл на сервере
    # with open('player_levels_data.csv', 'w') as file:
    # writer = csv.writer(file)
    players_level = PlayerLevel.objects.all()
    for player_level in players_level:
        player_id = player_level.player.player_id
        level_title = player_level.level.title
        is_completed = player_level.is_completed
        prize = LevelPrize.objects.filter(
            level=player_level.level
            ).first().prize.title if LevelPrize.objects.filter(
                level=player_level.level
                ).exists() else None
        writer.writerow({'Player_id': player_id,
                         'Level_title': level_title,
                         'Is_completed': is_completed,
                         'Prize': prize})

    response = HttpResponse(csv_buffer.getvalue(), content_type='text/csv')
    response['charset'] = 'utf-8'
    response['Content-Disposition'] = ('attachment; '
                                       'filename="player_levels_data.csv"')
    return response

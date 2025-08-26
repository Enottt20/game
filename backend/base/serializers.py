from rest_framework import exceptions, serializers

from base.models import LevelPrize, Level, Player, PlayerLevel


class PlayerGotPrizeSerializer(serializers.ModelSerializer):
    """Сериализатор достежений игрока."""

    player = serializers.ReadOnlyField(source='player.player_id')
    prize = serializers.StringRelatedField(source='player.prize')

    class Meta:
        model = PlayerLevel
        fields = ('player', 'prize')


class PlayerLevelSerializer(serializers.ModelSerializer):
    """Сериализатор уровня игрока."""

    class Meta:
        model = PlayerLevel
        fields = ('id', 'player', 'level',
                  'completed', 'is_completed', 'score')

    def create(self, validated_data):
        player_id = validated_data['player']
        level_id = validated_data['level']
        completed = validated_data.pop('completed')
        score = validated_data.pop('score')
        if completed:
            player = Player.objects.get(player_id=player_id)
            level = Level.objects.get(title=level_id)
            player_level = PlayerLevel.objects.create(
                player=player, level=level,
                completed=completed, score=score
                )
            player_level.is_completed = True
            player_level.save()
            level_prize = LevelPrize.objects.get(level=level)
            prize = level_prize.prize
            player.prize = prize
            player.save()
            return player_level
        else:
            raise exceptions.ValidationError(
                f'Игрок {player.player_id} не завершил уровень '
                f'{level_id.title} и не может получить приз '
                f'{prize.title}.'
                )

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return PlayerGotPrizeSerializer(instance, context=context).data


class LoaderPrizeSerializer(serializers.ModelSerializer):
    """Сериализатор загрузки данных в CSV-файл."""

    class Meta:
        model = PlayerLevel
        fields = ('player', 'level', 'is_completed')

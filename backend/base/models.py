from django.db import models


class Boost(models.Model):
    """Модель буста."""

    name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.CharField(
        max_length=150
    )

    def __str__(self):
        return self.name


class Prize(models.Model):
    """Модель приза."""

    title = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.title


class Player(models.Model):
    """Модель пользователя."""

    player_id = models.CharField(
        max_length=100,
        unique=True
    )
    launch_time = models.DateTimeField(
        auto_now_add=True
    )
    points = models.IntegerField(default=0)
    boost = models.ManyToManyField(
        Boost,
        through='PlayerBoost',
        related_name='player_boost',
        null=True,
        blank=True
    )
    prize = models.ForeignKey(
        Prize,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='player_prize'
    )

    def __str__(self):
        return self.player_id


class PlayerBoost(models.Model):
    """Модель для связи Player и Boost."""

    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='playerboost'
    )
    boost = models.ForeignKey(
        Boost,
        on_delete=models.CASCADE,
        related_name='playerboost'
    )

    def __str__(self):
        return f'{self.player.player_id} - {self.boost.name}'


class Level(models.Model):
    """Модель уровня."""

    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class LevelPrize(models.Model):
    """Модель приза за прохождение уровня."""

    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE
    )
    prize = models.ForeignKey(
        Prize,
        on_delete=models.CASCADE
    )
    received = models.DateField()

    def __str__(self):
        return self.level.title


class PlayerLevel(models.Model):
    """Модель уровня игрока."""

    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE
    )
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.player.player_id

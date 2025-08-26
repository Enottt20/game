from django.contrib import admin

from base.models import (Boost, Player, PlayerLevel, PlayerBoost,
                         Level, LevelPrize, Prize)


class BoostInline(admin.TabularInline):
    model = PlayerBoost
    min_num = 0


@admin.register(Boost)
class BoostAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')
    list_filter = ('name',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = (BoostInline,)
    list_display = ('player_id', 'launch_time', 'points', 'prize')
    fields = ('player_id', 'points', 'prize')
    list_filter = ('player_id',)


@admin.register(PlayerLevel)
class PlayerLevelAdmin(admin.ModelAdmin):
    list_display = ('player', 'level', 'completed', 'is_completed', 'score')
    fields = ('player', 'level', 'completed', 'is_completed', 'score')
    list_filter = ('player', 'level',)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    fields = ('title', 'order')
    list_filter = ('title',)


@admin.register(LevelPrize)
class LevelPrizeAdmin(admin.ModelAdmin):
    list_display = ('level', 'prize', 'received')
    fields = ('level', 'prize', 'received')
    list_filter = ('level',)


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title',)
    list_filter = ('title',)

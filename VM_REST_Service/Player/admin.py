from django.contrib import admin
from Player.models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'playerclass', 'email', 'level', 'position',)


admin.site.register(Player, PlayerAdmin)

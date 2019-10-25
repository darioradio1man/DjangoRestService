from django.db import models
from Player.models import Player


class Message(models.Model):
    class Meta:
        app_label = 'Message'

    playerFrom = models.ForeignKey(Player, verbose_name='From',
                                   related_name='playerFrom', on_delete=models.DO_NOTHING)
    playerTo = models.ForeignKey(Player, verbose_name='To',
                                 related_name='playerTo', on_delete=models.DO_NOTHING)
    messageText = models.TextField(verbose_name='Message Text', max_length=1000, blank=True)

    def __str__(self):
        return str(self.id)

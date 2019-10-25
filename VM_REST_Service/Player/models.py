from django.db import models
from GameMap.models import Location
from django.conf import settings

Choises_class = (
    ('Knight', 'Knight'),
    ('Wizard', 'Wizard'),
    ('Thief', 'Thief'),
    ('Paladin', 'Paladin')
)


class Player(models.Model):
    class Meta:
        app_label = 'Player'

    name = models.CharField(verbose_name='User name', max_length=30, blank=True)
    playerclass = models.CharField(verbose_name='Class', max_length=15, choices=Choises_class,
                                   default='Knight')
    email = models.CharField(verbose_name='Email', max_length=50, blank=True)
    level = models.IntegerField(verbose_name='Player level', default=0)
    position = models.ForeignKey(Location, default=1, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

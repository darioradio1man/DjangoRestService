from django.db import models

Location_type = (
    ('Forest', 'Forest'),
    ('Desert', 'Desert'),
    ('Dungeon', 'Dungeon'),
    ('River', 'River'),
    ('Ocean', 'Ocean')
)


class Location(models.Model):
    locationId = models.CharField(verbose_name='Location Id', max_length=10, unique=True, default='0-0')
    description = models.TextField(verbose_name='Location Description', blank=True)
    locationType = models.CharField(verbose_name='Location Type', max_length=15,
                                    choices=Location_type, default='Forest')

    def __str__(self):
        return self.locationId

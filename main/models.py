from django.db import models


class Location(models.Model):
    """
    Contains the JSON question
    """
    lat = models.CharField(max_length=32, null=True, blank=True)
    lon = models.CharField(max_length=32, null=True, blank=True)
    nick = models.CharField(max_length=32, null=True, blank=True)

    def __unicode__(self):
        return self.nick

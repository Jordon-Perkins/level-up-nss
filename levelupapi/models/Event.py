from django.db import models
from .Gamer import Gamer
from .Game import Game


class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    organizer = models.ForeignKey(Gamer, on_delete=models.SET_NULL, null=True, related_name='events_organizing')
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, null=True)
    time = models.TimeField(auto_now=False, null=True)
    attendees = models.ManyToManyField(Gamer, through='GamerEvent', related_name='events_attending')

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
from django.db import models
from .Gamer import Gamer
from .Game import Game


class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    organizer = models.ForeignKey(Gamer, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, null=True)
    time = models.TimeField(auto_now=False, null=True)
    
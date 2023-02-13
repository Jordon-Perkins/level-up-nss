from django.db import models
from .Gamer import Gamer
from .Event import Event

class GamerEvent(models.Model):
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
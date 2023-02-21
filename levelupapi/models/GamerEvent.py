from django.db import models
from .Gamer import Gamer
from .Event import Event

class GamerEvent(models.Model):
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name='gamer_event')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_gamer')
    
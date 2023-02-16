from django.db import models
from .GameType import GameType
from .Gamer import Gamer


class Game(models.Model):
    title = models.CharField(max_length=55)
    game_type = models.ForeignKey(GameType, on_delete=models.SET_NULL, null=True)
    number_of_players = models.IntegerField()
    skill_level = models.CharField(max_length=100)  # example being: ages 8 and up
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey(Gamer, on_delete=models.SET_NULL, null=True)

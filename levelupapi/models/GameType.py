from django.db import models

class GameType(models.Model):
    game_type = models.CharField(max_length=55)
    
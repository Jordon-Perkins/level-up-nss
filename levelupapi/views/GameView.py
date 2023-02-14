"""View module for handling requests about game"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, GameType


class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game 

        Returns:
            Response -- JSON serialized game 
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game 

        Returns:
            Response -- JSON serialized list of game 
        """
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)



class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game 
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'number_of_players', 'skill_level', 'maker', 'game_type')

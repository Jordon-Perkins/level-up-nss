"""View module for handling requests about event"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game


class EventView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized event
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        if "game" in request.query_params:
            events = Event.objects.filter(game_id = int(request.query_params['game']))
        else:
            events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        try:
            authenticated_player = Gamer.objects.get(user=request.auth.user)

        except Gamer.DoesNotExist:
            return Response({'message': 'You sent an invalid token'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            game = Game.objects.get(pk=request.data['gameId'])
        except Game.DoesNotExist:
            return Response({'message': 'You sent an invalid game  ID'}, status=status.HTTP_404_NOT_FOUND)

        event = Event.objects.create(
            date=request.data["date"],
            time=request.data["time"],
            description=request.data["description"],
            organizer=authenticated_player,
            game=game
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)


    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        event = Event.objects.get(pk=pk)
        event.date = request.data["date"]
        event.time = request.data["time"]
        event.description = request.data["description"]
    
        game = Game.objects.get(pk=request.data["game"])
        event.game = game
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GamerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gamer
        fields = ( 'full_name', )

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ( 'title', 'id')

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    organizer = GamerSerializer()
    game = GameSerializer()

    class Meta:
        model = Event
        fields = ('id', 'description', 'date', 'time', 'game', 'organizer', )

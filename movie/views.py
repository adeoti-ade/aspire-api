from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from movie.models import FavouriteQuote, Quote, Character, FavouriteCharacter
from .serializers import CharacterSerializer, QuoteSerializer, FavouriteQuoteSerializer, FavouriteCharacterSerializer


class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    @action(detail=True, methods=['get'])
    def quotes(self, request, pk=None):
        obj = self.get_object()
        quotes = obj.quote.all()
        quotes_serializer = QuoteSerializer(quotes, many=True)

        return Response(quotes_serializer.data)


from django.core.exceptions import ValidationError
from rest_framework import viewsets, generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

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

    @action(detail=True, methods=['post'], url_path="favorites")
    def favorites(self, request, pk=None):
        obj = self.get_object()
        user = request.user
        data = {
            "user": user.id,
            "character": obj.id
        }
        favourite_serializer = FavouriteCharacterSerializer(data=data)
        favourite_serializer.is_valid(raise_exception=True)
        favourite_serializer.save()

        return Response(favourite_serializer.data)

    @action(detail=True, methods=['post'], url_path="quotes/(?P<quotes_id>[\w-]+)/favorites")
    def favorite_quotes(self, request, quotes_id=None, pk=None, ):
        obj = self.get_object()
        quotes = self.validate_quote(quotes_id)
        if not quotes:
            raise serializers.ValidationError("quotes not found")
        if quotes.character != obj:
            raise serializers.ValidationError("quotes does not belong to character")
        user = request.user
        data = {
            "user": user.id,
            "quote": quotes.id
        }
        favourite_serializer = FavouriteQuoteSerializer(data=data)
        favourite_serializer.is_valid(raise_exception=True)
        favourite_serializer.save()

        return Response(favourite_serializer.data)

    def validate_quote(self, quotes_id):
        try:
            quote = Quote.objects.filter(id=quotes_id).first()
        except ValidationError:
            raise serializers.ValidationError(detail={
                "quote_id": ["not a valid quote id"]
            })

        return quote


class FavoriteAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        favourite_quote = user.favourite_quote.all()
        favourite_quote_serializer = FavouriteQuoteSerializer(favourite_quote, many=True)
        favourite_character = user.favourite_character.all()
        favourite_character_serializer = FavouriteCharacterSerializer(favourite_character, many=True)
        data = {
            "quotes": favourite_quote_serializer.data,
            "characters": favourite_character_serializer.data
        }
        return Response(data)


from movie.models import FavouriteQuote, Quote, Character, FavouriteCharacter

from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CharacterSerializer(BaseModelSerializer):
    class Meta:
        models = Character
        fields = "__all__"


class QuoteSerializer(BaseModelSerializer):
    class Meta:
        models = Quote
        fields = "__all__"


class FavouriteCharacterSerializer(BaseModelSerializer):
    class Meta:
        models = FavouriteCharacter
        fields = "__all__"


class FavouriteQuoteSerializer(BaseModelSerializer):
    class Meta:
        models = FavouriteQuote
        fields = "__all__"

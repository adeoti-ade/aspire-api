from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from data.character import data as character_data
from data.quotes import data as quote_data
from movie.models import FavouriteQuote, Quote, Character

User = get_user_model()

quotes_without_characters = []
for quote in quote_data:
    quote.pop("character")
    quotes_without_characters.append(quote)


class FavouriteQuoteTest(TestCase):
    def setUp(self):
        character_objects_list = [Character(**obj) for obj in character_data]
        self.character_objects = Character.objects.bulk_create(character_objects_list)
        self.user = User(email="dev@aspire.com", username="huntarhio")
        self.user.set_password("password")
        self.user.save()

    def test_create_favorite_character(self):
        character_zero = self.character_objects[0]
        character_one = self.character_objects[1]
        quote_zero_qs = Quote.objects.create(**quotes_without_characters[0], character=character_zero)
        quote_one_qs = Quote.objects.create(**quotes_without_characters[1], character=character_one)
        favourite_quote_zero = FavouriteQuote.objects.create(user=self.user,
                                                             quote=quote_zero_qs)
        favourite_quote_one = FavouriteQuote.objects.create(user=self.user, quote=quote_one_qs)
        self.assertEqual(favourite_quote_zero.quote, quote_zero_qs)
        self.assertEqual(favourite_quote_one.quote, quote_one_qs)

    def test_create_favorite_character_unique(self):
        character_zero = self.character_objects[0]
        quote_zero_qs = Quote.objects.create(**quotes_without_characters[0], character=character_zero)
        FavouriteQuote.objects.create(user=self.user,
                                      quote=quote_zero_qs)
        with self.assertRaises(IntegrityError):
            FavouriteQuote.objects.create(user=self.user,
                                          quote=quote_zero_qs)

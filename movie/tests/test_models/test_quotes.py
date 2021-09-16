from django.test import TestCase
from django.db.utils import IntegrityError

from movie.models import Quote, Character
from data.character import data as character_data
from data.quotes import data as quote_data


class QuoteModelTestCase(TestCase):
    def setUp(self):
        self.data = quote_data

    def test_create_quotes_no_character(self):
        quotes_without_characters = []
        for obj in self.data:
            obj.pop("character")
            quotes_without_characters.append(obj)
        quote_objects = [Quote(**obj) for obj in quotes_without_characters]
        with self.assertRaises(IntegrityError):
            Quote.objects.bulk_create(quote_objects)

    def test_create_quotes_success(self):
        character = character_data[0]
        character_qs = Character.objects.create(**character)
        quote_qs = Quote.objects.create(**quote_data[0], character=character_qs)
        self.assertEqual(type(quote_qs), Quote)


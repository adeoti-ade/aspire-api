from django.test import TestCase
from django.db.utils import IntegrityError

from movie.models import Quote, Character
from data.character import data as character_data


class CharacterModelTestCase(TestCase):
    def setUp(self):
        self.data = [
            {
                "_id": "5cd96e05de30eff6ebccf13f",
                "dialog": "One thing I've learnt about Hobbits: They are a most hardy folk.",
            },
            {
                "_id": "5cd96e05de30eff6ebccf140",
                "dialog": "Foolhardy maybe. He's a Took!",
            }
        ]

    def test_create_quotes_no_character(self):
        quote_objects = [Quote(**obj) for obj in self.data]
        with self.assertRaises(IntegrityError):
            Quote.objects.bulk_create(quote_objects)

    def test_create_quotes_success(self):
        # character_objects = [Character(**obj) for obj in self.data]
        Character.objects.create(**character_data[0])
        retrieved_character = Character.objects.get(_id="5cd99d4bde30eff6ebccfbbe")
        self.assertEqual(type(retrieved_character), Character)
    #
    # def test_get_character_by_id_from_oneapi_not_found(self):
    #     character_objects = [Character(**obj) for obj in self.data]
    #     Character.objects.bulk_create(character_objects)
    #     with self.assertRaises(Character.DoesNotExist):
    #         Character.objects.get(_id="5cd99d4bde30eff6ebccf")

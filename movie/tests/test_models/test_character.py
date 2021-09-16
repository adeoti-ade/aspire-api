from django.test import TestCase

from movie.models import Character


class CharacterModelTestCase(TestCase):
    def setUp(self):
        self.data = [
            {
                "_id": "5cd99d4bde30eff6ebccfbbe",
                "height": "",
                "race": "Human",
                "gender": "Female",
                "birth": "",
                "spouse": "Belemir",
                "death": "",
                "realm": "",
                "hair": "",
                "name": "Adanel",
            },
            {
                "_id": "5cd99d4bde30eff6ebccfbbf",
                "height": "",
                "race": "Human",
                "gender": "Male",
                "birth": "Before ,TA 1944",
                "spouse": "",
                "death": "Late ,Third Age",
                "realm": "",
                "hair": "",
                "name": "Adrahil I",
            }
        ]

    def test_create_character(self):
        character_objects = [Character(**obj) for obj in self.data]
        character_objects = Character.objects.bulk_create(character_objects)
        self.assertEqual(type(character_objects[0]), Character)

    def test_get_character_by_id_from_oneapi(self):
        character_objects = [Character(**obj) for obj in self.data]
        Character.objects.bulk_create(character_objects)
        retrieved_character = Character.objects.get(_id="5cd99d4bde30eff6ebccfbbf")
        self.assertEqual(type(retrieved_character), Character)

    def test_get_character_by_id_from_oneapi_not_found(self):
        character_objects = [Character(**obj) for obj in self.data]
        Character.objects.bulk_create(character_objects)
        with self.assertRaises(Character.DoesNotExist):
            Character.objects.get(_id="5cd99d4bde30eff6ebccf")

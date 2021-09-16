from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from data.character import data as character_data
from movie.models import FavouriteCharacter, Character

User = get_user_model()


class FavouriteCharacterTest(TestCase):
    def setUp(self):
        character_objects = [Character(**obj) for obj in character_data]
        self.character_objects = Character.objects.bulk_create(character_objects)
        self.user = User(email="dev@aspire.com", username="huntarhio")
        self.user.set_password("password")
        self.user.save()

    def test_create_favorite_character(self):
        character_zero = self.character_objects[0]
        character_one = self.character_objects[1]
        favourite_character_zero = FavouriteCharacter.objects.create(user=self.user,
                                                                     character=self.character_objects[0])
        favourite_character_one = FavouriteCharacter.objects.create(user=self.user, character=self.character_objects[1])
        self.assertEqual(favourite_character_zero.character, character_zero)
        self.assertEqual(favourite_character_one.character, character_one)

    def test_create_favorite_character_unique(self):
        character_zero = self.character_objects[0]
        character_one = self.character_objects[1]
        FavouriteCharacter.objects.create(user=self.user,
                                          character=character_zero)
        with self.assertRaises(IntegrityError):
            FavouriteCharacter.objects.create(user=self.user,
                                              character=character_zero)

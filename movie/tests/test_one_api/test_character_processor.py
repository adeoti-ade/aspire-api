from django.test import TestCase

from movie.services.oneapi.character import CharacterProcessor


class CharacterProcessorTestCase(TestCase):
    def setUp(self):
        self.character_processor = CharacterProcessor()

    def test_process_request(self):
        response_data = self.character_processor.process_request()
        self.assertIsNotNone(response_data)
        self.assertEqual(dict, type(response_data))

    def test_process_characters(self):
        response_data = self.character_processor.process_characters()
        self.assertIsNotNone(response_data)
        self.assertEqual(list, type(response_data))

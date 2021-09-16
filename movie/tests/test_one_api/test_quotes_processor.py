from django.test import TestCase

from movie.services.oneapi.quotes import QuotesProcessor



class QuoteProcessorTestCase(TestCase):
    def setUp(self):
        self.quote_processor = QuotesProcessor()

    def test_process_request(self):
        response_data = self.quote_processor.process_request()
        self.assertIsNotNone(response_data)
        self.assertEqual(dict, type(response_data))

    def test_process_characters(self):
        response_data = self.quote_processor.process_quotes()
        self.assertIsNotNone(response_data)
        self.assertEqual(list, type(response_data))

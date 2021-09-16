from django.core.management.base import BaseCommand
from django.db import transaction
from movie.models import Character, Quote
from movie.services.oneapi.quotes import QuotesProcessor


class Command(BaseCommand):
    help = 'fetch and store characters from one api character endpoint'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        Quote.objects.all().delete()
        self.stdout.write("deleted quotes")
        quotes_processor = QuotesProcessor()
        response_data = quotes_processor.process_quotes()
        quote_objects = []
        for obj in response_data:
            character_id = obj.get("character")
            character = Character.objects.filter(_id=character_id).first()
            obj.pop("character")
            quote_objects.append(Quote(**obj, character=character))

        Quote.objects.bulk_create(quote_objects)
        self.stdout.write(f"created {len(response_data)} quotes")

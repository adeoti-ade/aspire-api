from django.core.management.base import BaseCommand
from django.db import transaction
from movie.models import Character
from movie.services.oneapi import CharacterProcessor


class Command(BaseCommand):
    help = 'fetch and store characters from one api character endpoint'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        Character.objects.all().delete()
        self.stdout.write("deleted characters")
        character_processor = CharacterProcessor()
        response_data = character_processor.process_characters()
        character_objects = [Character(**obj) for obj in response_data]
        Character.objects.bulk_create(character_objects)
        self.stdout.write(f"created {len(response_data)} characters")

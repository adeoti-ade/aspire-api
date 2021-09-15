from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = 'fetch and store characters from one api character endpoint'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # self.stdout.write("deleted all credit card approval limit config objects")
        # self.stdout.write(f"created {len(seed_data)} credit card approval limit config objects")
        pass

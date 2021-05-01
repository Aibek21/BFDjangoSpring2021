from django.core.management.base import BaseCommand
from main.models import Book
import random


class Command(BaseCommand):
    help = 'Management command to seed books'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Total number of books to create')
        parser.add_argument('-p', '--prefix', type=str, help='Prefix for books to create')
        parser.add_argument('-b', '--big', action='store_true', help='Create big books')

    def handle(self, *args, **options):
        count = options.get('count')
        prefix = options.get('prefix')
        big = options.get('big')

        if prefix is None:
            prefix = 'Book'

        for i in range(count):
            if big:
                Book.objects.create(title=f'{prefix} {i}', num_pages=5000)
            else:
                Book.objects.create(title=f'{prefix} {i}', num_pages=random.randint(100, 2000))
            self.stdout.write(f'{prefix} {i} created')

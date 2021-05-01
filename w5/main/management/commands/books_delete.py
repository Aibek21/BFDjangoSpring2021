from django.core.management.base import BaseCommand
from main.models import Book
import random


class Command(BaseCommand):
    help = 'Management command to delete books'

    def add_arguments(self, parser):
        parser.add_argument('book_ids', nargs='+', type=int, help='Total number of books to create')

    def handle(self, *args, **options):
        book_ids = options.get('book_ids')

        for b_id in book_ids:
            try:
                book = Book.objects.get(id=b_id)
                book.delete()
                self.stdout.write(self.style.SUCCESS(f'Book with id {b_id} deleted'))
            except Book.DoesNotExist as e:
                self.stdout.write(self.style.ERROR(f'Book with id {b_id} does not exist!'))

        # if prefix is None:
        #     prefix = 'Book'
        #
        # for i in range(count):
        #     if big:
        #         Book.objects.create(title=f'{prefix} {i}', num_pages=5000)
        #     else:
        #         Book.objects.create(title=f'{prefix} {i}', num_pages=random.randint(100, 2000))
        #     self.stdout.write(f'{prefix} {i} created')

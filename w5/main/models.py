from django.db import models
from rest_framework import serializers


class Publisher(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    # first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    # last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    website = models.CharField(max_length=100, null=True, blank=True, verbose_name='Веб сайт')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Город')
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Страна')

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

    def __str__(self):
        return self.name

    # @property
    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фамилия')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Email')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class BookManager(models.Manager):

    def get_by_author_with_relation(self, author_id):
        return self.get_related().filter(author_id=author_id)

    def get_by_author_without_relation(self, author_id):
        return self.filter(author_id=author_id)

    def get_related(self):
        return self.select_related('author', 'publisher')


class BookQuerySet(models.QuerySet):

    def get_by_author(self, author_id):
        return self.get_related().filter(author_id=author_id)

    def get_related(self):
        return self.select_related('author', 'publisher')


def num_pages_range_validation(value):
    if not (1 <= value <= 2000):
        raise serializers.ValidationError('Invalid num_pages value')


class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    publication_date = models.DateField(null=True, blank=True, verbose_name='Дата публикации')
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц',
                                    validators=[num_pages_range_validation])
    is_active = models.BooleanField(default=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT, null=True, blank=True, verbose_name='Издатель')

    # objects = BookManager()
    objects = BookQuerySet.as_manager()

    class Meta:
        ordering = ['-publication_date']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        # abstract = True

    def check_num_pages(self):
        if self.num_pages > 10:
            return True
        return False

    @classmethod
    def active_books(cls):
        cls.objects.filter(is_active=True)

    @staticmethod
    def compare_books(b1, b2):
        return b1.num_pages > b2.num_pages

# class HardBook(Book):
#     width = models.IntegerField()
#     height = models.IntegerField()
#
#
# class EBook(Book):
#     size = models.IntegerField()

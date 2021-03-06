from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    website = models.CharField(max_length=100, null=True, blank=True, verbose_name='Веб сайт')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Город')
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Страна')

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

    def __str__(self):
        return self.name


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


class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    publication_date = models.DateField(verbose_name='Дата публикации')
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц')
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name='books', verbose_name='Автор')
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT, related_name='books', verbose_name='Издатель')

    # objects = BookManager()
    objects = BookQuerySet.as_manager()

    class Meta:
        ordering = ['-publication_date']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

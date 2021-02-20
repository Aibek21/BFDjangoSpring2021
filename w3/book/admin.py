from django.contrib import admin
from book.models import Book, Author, Publisher


# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Publisher)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_date', 'author', 'publisher', ]
    ordering = ['title']
    search_fields = ['title', 'author__first_name', 'author__last_name', ]
    list_filter = ['publication_date', 'publisher', ]

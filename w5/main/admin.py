from django.contrib import admin
from main.models import Book, Author, Publisher
from django.contrib.admin import ModelAdmin

# Register your models here.
# admin.site.register(HardBook)
# admin.site.register(EBook)
# admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('id', 'title', 'num_pages')

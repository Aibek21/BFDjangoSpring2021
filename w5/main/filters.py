from django_filters import rest_framework as filters
from main.models import Book


class BookFilter(filters.FilterSet):
    # Book.objects.filter(title__contains=value)
    # LIKE '%value%'
    title = filters.CharFilter(lookup_expr='contains')

    # Book.objects.filter(num_pages__gte=value)
    # num_pages >= value
    min_pages = filters.NumberFilter(field_name='num_pages', lookup_expr='gte')

    # Book.objects.filter(num_pages__lte=value)
    # num_pages <= value
    max_pages = filters.NumberFilter(field_name='num_pages', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ('title', 'num_pages', 'min_pages', 'max_pages',)

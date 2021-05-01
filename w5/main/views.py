import logging
from django.db.models import Avg, Max, Min, Sum, Count
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from main.models import Book, Author, Publisher
from main.serializers import BookSerializer, AuthorSerializer, BookFullSerializer, PublisherSerializer
from main.permissions import PublisherPermission, AuthorPermission

logger = logging.getLogger(__name__)


class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    # queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = LimitOffsetPagination

    # filter_backends = (DjangoFilterBackend,
    #                    filters.SearchFilter,
    #                    filters.OrderingFilter)

    # used by DjangoFilterBackend
    # filterset_fields = ('title', 'num_pages',)
    # filterset_class = BookFilter

    # used by SearchFilter
    # search_fields = ('title', 'num_pages',)

    # ordering_fields = ('title', 'num_pages',)

    def get_queryset(self):
        return Book.objects.select_related('publisher')

    def get_serializer_class(self):
        if self.action == 'list':
            return BookFullSerializer
        return BookSerializer

    # def get_permissions(self):
    #     logger.debug('get_permissions')
    #     if self.action == 'create':
    #         permission_classes = [PublisherPermission]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Book object created, ID: {serializer.instance}')
        logger.info(f'Book object created, ID: {serializer.instance}')
        logger.warning(f'Book object created, ID: {serializer.instance}')
        logger.error(f'Book object created, ID: {serializer.instance}')
        logger.critical(f'Book object created, ID: {serializer.instance}')

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = (AllowAny,)
    #     else:
    #         permission_classes = (IsAuthenticated,)
    #
    #     return [permission() for permission in permission_classes]

    # def list(self, request):
    #     serializer = BookSerializer(self.get_queryset(), many=True)
    #     return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='inactive', url_name='in_active',
            permission_classes=(AuthorPermission,))
    def not_active(self, request):
        logger.debug('not_active')
        # filter = BookFilter(request.GET, queryset=Book.objects.all())
        # queryset = Book.objects.filter(is_active=False)
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    def create_book(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response('OK')

    @action(methods=['GET'], detail=False, permission_classes=(AllowAny,))
    def book_report(self, request):
        queryset = Book.objects.aggregate(avg_pages=Avg('num_pages'), max_pages=Max('num_pages'),
                                          min_pages=Min('num_pages'), sum_pages=Sum('num_pages'))

        # data = {
        #     'avg': Book.objects.aggregate(Avg('num_pages'))['num_pages__avg'],
        #     'max': Book.objects.aggregate(max_pages=Max('num_pages'))['max_pages'],
        #     'min': Book.objects.aggregate(Min('num_pages'))['num_pages__min'],
        #     'sum': Book.objects.aggregate(Sum('num_pages'))['num_pages__sum']
        # }

        data = {
            'avg': queryset['avg_pages'],
            'max': queryset['max_pages'],
            'min': queryset['min_pages'],
            'sum': queryset['sum_pages'],
        }
        return Response(data)


class AuthorApiViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class PublisherApiViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.prefetch_related('books')
    # queryset = Publisher.objects.annotate(books_count=Count('books'),
    #                                       max_pages=Max('books__num_pages'))
    serializer_class = PublisherSerializer
    permission_classes = (AllowAny,)

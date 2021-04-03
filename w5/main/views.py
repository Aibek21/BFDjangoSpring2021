from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from main.models import Book, Author
from main.serializers import BookSerializer, AuthorSerializer, BookFullSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from main.filters import BookFilter
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.decorators import api_view


class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
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
        return Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BookFullSerializer
        return BookSerializer

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

    @action(methods=['GET'], detail=False, url_path='inactive', url_name='in_active', permission_classes=(AllowAny,))
    def not_active(self, request):
        # filter = BookFilter(request.GET, queryset=Book.objects.all())
        # queryset = Book.objects.filter(is_active=False)
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    def create_book(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response('OK')


class AuthorApiView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
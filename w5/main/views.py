from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from main.models import Book, Author
from main.serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action


class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    # queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

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
        # queryset = Book.objects.filter(is_active=False)
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class AuthorApiView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

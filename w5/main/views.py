from django.shortcuts import render
from rest_framework import generics, mixins
from main.models import Book, Author
from main.serializers import BookSerializer, AuthorSerializer


class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class AuthorApiView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

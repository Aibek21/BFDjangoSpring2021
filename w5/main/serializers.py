from rest_framework import serializers
from main.models import Book, Author, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(required=True)
    # publisher = PublisherSerializer()
    title = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ('id', 'title', 'publication_date',)


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'email', 'books')

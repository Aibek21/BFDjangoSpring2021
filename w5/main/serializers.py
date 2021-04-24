from rest_framework import serializers
from main.models import Book, Author, Publisher


class PublisherSerializer(serializers.Serializer):
    first_name = serializers.CharField(write_only=True)
    address = serializers.CharField(read_only=True)

    # class Meta:
    #     model = Publisher
    #     fields = '__all__'

    # def to_internal_value(self, data):
    #     #return instance
    #     pass
    #
    # def to_representation(self, instance):
    #     #convert instance to dict
    #     #return data
    #     pass
    #
    # def create(self, validated_data):
    #     #create instance
    #     #Publisher.objects.create(**validated_data)
    #     #return instance
    #     pass
    #
    # def update(self, instance, validated_data):
    #     #update instance
    #     return instance


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(required=True)
    # publisher = PublisherSerializer()
    publication_date = serializers.DateField(read_only=True)

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ('id', 'title', 'publication_date', 'num_pages')
        # exclude = ('is_active')

    # def validate(self, attrs):
    #     print(attrs)
    #     return attrs

    # def validate_num_pages(self, value):
    #     if value < 1:
    #         raise serializers.ValidationError('num_pages must be positive')
    #     return value

    # def validate_title(self, value):
    #     if '_' in value:
    #         raise serializers.ValidationError('invalid chars in title')
    #     return value

    # def create(self, validated_data):
    #     #get author from validated_data
    #     # create author
    #     # create book
    #     #return book
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass


class BookFullSerializer(BookSerializer):
    # author = AuthorSerializer(required=True)
    publisher = PublisherSerializer()

    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields + ('publisher',)


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'email', 'books', 'photo')

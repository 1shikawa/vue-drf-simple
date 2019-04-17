from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from book.models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class BookSerializer(WritableNestedModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'price', 'authors')

from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name"]


class BookSerializer(serializers.ModelSerializer):
    """
    Сериализатор для книги с полем author_id.
    """

    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True
    )

    class Meta:
        model = Book
        fields = ["id", "title", "author", "author_id", "count"]

    def create(self, validated_data):
        """
        Создание книги с привязкой к автору.
        """

        author = validated_data.pop("author_id")
        book = Book.objects.create(author=author, **validated_data)

        return book

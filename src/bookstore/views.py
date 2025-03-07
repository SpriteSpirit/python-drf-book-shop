from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Управление авторами
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Управление книгами
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self) -> QuerySet:
        """
        Список книг, если указан author_id в запросе
        """

        queryset = super().get_queryset()
        author_id = self.request.query_params.get("author_id")

        if author_id:
            queryset = queryset.filter(author_id=author_id)

        return queryset

    @action(detail=True, methods=["post"])
    def buy(self, request, pk=None) -> Response:
        """
        Покупка книги
        """

        book = self.get_object()

        if book.count <= 0:
            return Response(
                {"error": "Book out of stock"}, status=status.HTTP_400_BAD_REQUEST
            )

        book.count -= 1
        book.save()

        return Response({"message": "Book purchased", "count": book.count})

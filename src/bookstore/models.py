from django.db import models


class Author(models.Model):
    """
    Автор
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    """
    Книга
    """

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

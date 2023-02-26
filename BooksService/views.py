
from rest_framework import viewsets

from BooksService.models import Book
from BooksService.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

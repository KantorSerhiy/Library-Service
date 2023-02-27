from rest_framework import serializers

from BooksService.serializers import BookSerializer
from Borrowing.models import Borrowing


class BorrowingReadSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False, read_only=True)

    class Meta:
        model = Borrowing
        fields = "__all__"
        
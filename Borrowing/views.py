from django.shortcuts import render
from rest_framework import mixins, viewsets

from BooksService.permissions import IsAdminUserOrReadOnly
from Borrowing.models import Borrowing
from Borrowing.serializers import BorrowingReadSerializer


class BorrowingViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingReadSerializer
    permission_classes = [IsAdminUserOrReadOnly]

from django.urls import path
from rest_framework import routers

from Borrowing.views import BorrowingViewSet

router = routers.SimpleRouter()
router.register("borrowing", BorrowingViewSet)



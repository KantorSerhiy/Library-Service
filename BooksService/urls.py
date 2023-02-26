from django.urls import path, include
from rest_framework import routers

from BooksService.views import BookViewSet

router = routers.SimpleRouter()
router.register("books", BookViewSet)





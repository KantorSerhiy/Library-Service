from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Users.views import CreateUserView, ManageUserView

urlpatterns = [
    path("", CreateUserView.as_view(), name="create-user"),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("me/", ManageUserView.as_view(), name="me"),
]

app_name = "Users"

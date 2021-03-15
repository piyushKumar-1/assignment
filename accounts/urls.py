from django.urls import path
from .views import CreateUserAPIView, LoginAPI

app_name="accounts"

urlpatterns = [
    path('user/register/', CreateUserAPIView.as_view(), name="register"),
    path('user/login/', LoginAPI.as_view(), name="login"),
]

from django.urls import path, include
from . import views
urlpatterns = [
    path('auth/signup', views.UserCreateAPIView.as_view()),
    path('auth/login', views.UserLoginViewJWT.as_view())
]
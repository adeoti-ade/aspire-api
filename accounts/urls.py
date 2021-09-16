from django.urls import path, include
from . import views
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register', views.UserCreateAPIView.as_view()),
    path('auth/login', views.UserLoginViewJWT.as_view())
]

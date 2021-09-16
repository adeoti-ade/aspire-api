from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'character', views.CharacterViewSet)
app_name = 'movie'

urlpatterns = [
    path('favorites', views.FavoriteAPIView.as_view())
]

urlpatterns += router.urls

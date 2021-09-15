from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movie/', include('movie.urls')),
    path('api/accounts/', include('accounts.urls')),
]

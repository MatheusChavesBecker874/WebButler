from django.contrib import admin
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("projeto.urls")),
]

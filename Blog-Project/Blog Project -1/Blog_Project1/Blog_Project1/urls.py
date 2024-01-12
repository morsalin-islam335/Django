
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage,  name = 'homepage'),
    path("categories/", include("categories.urls")),
    path("post/", include("post.urls")),
    path("profiles/", include("profiles.urls")),
    path("author/", include("author.urls")),
]

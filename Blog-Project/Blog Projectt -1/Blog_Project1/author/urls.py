from django.urls import path

from author.views import addAuthor
    # path("addCategories/", addCategories, name= 'addCategories'),
urlpatterns = [
    path('add/', addAuthor, name='add_author')
]

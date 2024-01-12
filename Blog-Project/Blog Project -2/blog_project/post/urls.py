from django.urls import path

from post import views
urlpatterns = [
    # path("addCategories/", addCategories, name= 'addCategories'),
    path("add_post/", views.addPost, name='add_post'),
    path("edit_post/<int:id>",views.editPost, name='edit_post'),
    path("delete_post/<int:id>", views.deletePost, name='delete_post'),
]

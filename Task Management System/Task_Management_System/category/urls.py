from django.urls import path

from category import views
urlpatterns = [
    path("addCategory/", views.addCategory, name = 'addCategory'),

]

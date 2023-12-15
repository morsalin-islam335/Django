from django.urls import path, include

from . import views

urlpatterns = [
    path("",views.home),
    path("details/",views.details),
    path("contact/",views.contact),
]

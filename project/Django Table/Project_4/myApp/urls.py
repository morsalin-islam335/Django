from django.urls import path

from . import views
# from . import djangoForm



urlpatterns = [
    path("",views.home, name = "homepage"),
    path("about/", views.about, name = "about"),
    path("form/", views.form, name = "form"),
    path("djangoForm/", views.DjangoForm, name = "djangoForm"),
]

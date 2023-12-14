
from django.contrib import admin
from django.urls import path
from .views import aboutMe
from  . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("aboutme/",aboutMe),  # automatic triger function in views
    path("",views.homePage),
]

from django.urls import path

from .views import home,getCookie, deleteCookie

urlpatterns = [
    path("",home, name = 'homepage'),
    path("get/",getCookie, name = 'getCookies'),
    path("del/",deleteCookie, name = 'deleteCookies'),
]

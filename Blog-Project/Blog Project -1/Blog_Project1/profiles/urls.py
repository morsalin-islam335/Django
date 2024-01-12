from django.urls import path 


from profiles.views import addProfile

urlpatterns = [
    path("addProfile/",  addProfile, name = "addProfile"),
]

from django.urls import path

from . import views
urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("sign-up/", views.sign_up_page, name = 'sign-up'),
    path("profile/",views.profile, name = 'profile'),
    path('login/', views.userLogin, name = 'login'),
    path('logout/', views.userLogout, name = 'logout'),
    path('changePasswordWithOldPassword/', views.changePasswordWithOldPassword, name = 'changePasswordWithOldPassword'),
    path('changePasswordWithOutOldPassword/', views.changePasswordWithOutOldPassword, name = 'changePasswordWithOutOldPassword'),
    path('editProfile', views.EditProfileInfo, name = "editProfile"),
    path('showProfile', views.showProfile, name = "showProfile"),
]

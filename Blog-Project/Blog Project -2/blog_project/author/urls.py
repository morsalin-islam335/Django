from django.urls import path

from author import views
urlpatterns = [
    path('sign_up/', views.Signup, name='sign_up'),
    path('login/', views.loginForm, name = 'login'),
    path('logout/', views.userLogout, name = 'logout'),
    path('editProfile/', views.updateProfile, name = 'editProfile'),
    path("profile/", views.Profile, name = 'profile'),
    path("changePassword/", views.changePassword, name = "changePassword")
]

from django.urls import path

from task import views

urlpatterns = [
    path("", views.home, name = 'homepage'),
    path("addTask/", views.addTask, name = 'addTask'),
    path('editTask/<int:id>/', views.editTask, name = 'editTask'),
    path('deleteTask/<int:id>/', views.deleteTask, name= 'deleteTask'),

]

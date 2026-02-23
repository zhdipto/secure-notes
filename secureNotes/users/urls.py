from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginCheck, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('createNote/', views.createNote, name='createNote'),
    path('logout/', views.logoutView, name='logoutView'),
    path('delete-note/<int:pk>/', views.delete_note, name='deleteNote'),
]
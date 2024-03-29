from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('note/<str:pk>', views.getNote),
    path('notes/create/', views.createNote),
    path('notes/<str:pk>/update', views.updateNote),
    path('notes/<str:pk>/delete', views.deleteNote),
    path('register/',RegisterUser.as_view()),
]
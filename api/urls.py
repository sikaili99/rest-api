from django.urls import path
from api import views

urlpatterns = [
    path('note/create/', views.create_note),
    path('notes/list/', views.get_notes),
    path('note/<str:pk>/', views.get_note),
    path('note/<str:pk>/update/', views.update_note),
    path('note/<str:pk>/delete/', views.delete_note),
]

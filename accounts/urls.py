from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/<int:pk>/edit/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('users/<int:pk>/delete/confirm/', views.delete_confirm, name='delete_confirm'),
]

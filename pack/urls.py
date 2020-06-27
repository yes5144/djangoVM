from django.urls import path
from . import views

urlpatterns = [
    path('pack/<int:nid>/', views.pack),
    path('', views.index),
]
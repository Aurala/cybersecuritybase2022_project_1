from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('memez/brag/<int:user>/', views.brag, name='brag'),
]

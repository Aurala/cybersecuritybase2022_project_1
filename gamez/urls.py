from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('brag/<int:user>/', views.bragView, name='brag'),
    path('delete/<int:id>', views.deleteView, name='delete'),
    path('new/', views.newView, name='new'),
    path('new/add/', views.addView, name='add'),
    path('backup/', views.backupView, name='backup'),
    path('upload/', views.uploadView, name='upload'),
    path('upload/restore/', views.restoreView, name='restore'),
]

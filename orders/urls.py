from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<uuid:id>/', views.show, name='show'),
    path('<uuid:id>/edit/', views.edit, name='edit'),
    path('<uuid:id>/delete/', views.delete, name='delete'),
]

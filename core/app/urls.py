from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('detail/<int:pk>/', views.detail_view, name='detail'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('food_create/', views.food_create, name='food_create'),
    path('delete/<int:pk>/', views.delete_food, name='delete')
]

from django.urls import path
from . import views

urlpatterns = [
  path('', views.wish_index, name='index'),
  path('item/create/', views.ItemCreate.as_view(), name='item_create'),
  path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
]

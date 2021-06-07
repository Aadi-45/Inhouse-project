from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('product/<int:id>/', views.productView, name="product"),
    path('profile/', views.profileView, name="profile"),
    path('cart/', views.cartView, name="cart"),
]

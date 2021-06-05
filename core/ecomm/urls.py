from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('product/<int:id>/', views.productView, name="product"),
    path('personal/', views.profileView, name="profile"),
]

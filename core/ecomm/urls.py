from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('product/<int:id>/', views.product_view, name="product"),
    path('personal/', views.test_view,name="presonal"),
]

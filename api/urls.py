from django.urls import  path
from . import views

urlpatterns = [
    path('users', views.getUsers, name="users"),
    path('products', views.getProducts, name="products"),
    path('categories', views.getCategories, name="categories"),
]

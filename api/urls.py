from django.urls import  path
from . import views

urlpatterns = [
    path('users/', views.getUsers, name="users"),
    path('users/<pk>', views.getUser, name="user"),
    path('products/', views.getProducts.as_view(), name="products"),
    path('products/<pk>', views.getProduct, name="product"),
    path('categories/', views.getCategories, name="categories"),
    path('categories/<pk>', views.getCategory, name="category"),
]

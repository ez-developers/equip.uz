from django.urls import  path
from . import views

urlpatterns = [
    path('users/', views.getUsers, name="users"),
    path('users/<pk>', views.getUser, name="user"),
    path('products/', views.productsList.as_view(), name="products"),
    path('products/<pk>', views.productDetail.as_view(), name="product"),
    path('categories/', views.getCategories, name="categories"),
    path('categories/<pk>', views.getCategory, name="category"),
]

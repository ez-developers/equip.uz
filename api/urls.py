from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.usersList.as_view(), name="users"),
    path('users/<pk>', views.userDetail.as_view(), name="user"),
    path('products/', views.productsList.as_view(), name="products"),
    path('products/<pk>', views.productDetail.as_view(), name="product"),
    path('categories/', views.categoryList.as_view(), name="categories"),
    path('categories/<pk>', views.categoryDetail.as_view(), name="category"),
]

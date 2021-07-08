from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.usersList.as_view(), name="users"),
    path('users/<pk>', views.userDetail.as_view(), name="user"),
    path('products/', views.productsList.as_view(), name="products"),
    path('categories/', views.cateogriesList.as_view(), name="categories"),
]

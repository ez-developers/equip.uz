from django.urls import path
from . import views

urlpatterns = [
    path('adduser/', views.userAdd.as_view(), name='adduser'),
    path('users/', views.usersList.as_view(), name="users"),
    path('users/<pk>', views.userDetail.as_view(), name="user"),
    path('products/', views.productsList.as_view(), name="products"),
    path('categories/', views.categoriesList.as_view(), name="categories"),
    path('promo/', views.promoList.as_view(), name="promos"),
    path('promo/<pk>', views.promoDetail, name="promo")
]

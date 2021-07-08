from django.contrib import admin
from .models import User, Category, Product
from django.utils.html import format_html

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "first_name", "last_name")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'colored_price', 'colored_category')
    list_filter = ("category", )


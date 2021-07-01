from django.contrib import admin
from .models import User, Category, Product

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "first_name", "last_name")


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    pass

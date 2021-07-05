from django.contrib import admin
from .models import User, Category, Product

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "first_name", "last_name")

    def has_add_permission(self, request):
        return False

    def has_edit_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    pass

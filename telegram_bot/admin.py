from django.contrib import admin
from .models import User, Category, Product
from django.utils.html import format_html
from django.contrib.admin import AdminSite

# Register your models here.
admin.site.site_url = None
admin.site.index_title = "Добро пожаловать!"
admin.site.site_title = "Администрация «Equip Uz»"
admin.site.site_header = "Администрация «Equip Uz»"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "name", "username",
                    "phone_number", "notifications")
    list_display_links = ("user_id",)
    change_form_template = 'admin/change_form.html'

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name", )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'colored_price', 'colored_category')
    list_filter = ("category", )
    search_fields = ("name", )

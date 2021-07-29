from django.contrib import admin
from .models import Promo, User, Category, Product
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
    search_fields = ("name", )
    change_form_template = 'admin/change_form.html'

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name", )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'category')
    list_filter = ("category", )
    search_fields = ("name", )


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):

    list_display = ('name', 'date_published')

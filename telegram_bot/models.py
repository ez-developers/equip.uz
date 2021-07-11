from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class User(models.Model):
    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"

    user_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.CharField(max_length=9, null=True, blank=False)
    username = models.CharField(max_length=20, null=True, blank=False)
    joined_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    notifications = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user_id)


class Category(models.Model):
    name = models.CharField(
        verbose_name="Название категории", max_length=255, null=True)

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категорию"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        verbose_name="Название продукта", max_length=255, null=True)
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(
        verbose_name="Цена", max_digits=6, decimal_places=2, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория", null=True)

    @admin.display
    def colored_price(self):
        return format_html(
            '<span style="font-weight:bold; color:#FFA500;">{}</span>',
            self.price,
        )

    @admin.display
    def colored_category(self):
        return format_html(
            '<b>{}</b>',
            self.category,
        )

    class Meta:
        verbose_name_plural = "Продукты"
        verbose_name = "Продукт"

    def __str__(self):
        return self.name

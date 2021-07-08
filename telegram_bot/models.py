from django.db import models
from django.contrib import admin 
from django.utils.html import format_html


class User(models.Model):
    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"

    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=False)
    phone_number = models.BigIntegerField()
    username = models.CharField(max_length=20, null=True, blank=False)
    joined_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
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

    
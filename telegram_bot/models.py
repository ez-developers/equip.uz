from django.db import models

# Create your models here.


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
        return self.name


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

    class Meta:
        verbose_name_plural = "Продукты"
        verbose_name = "Продукт"

    def __str__(self):
        return self.name

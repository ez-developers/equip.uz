from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class User(models.Model):
    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"

    user_id = models.BigIntegerField(
        primary_key=True, verbose_name="ID пользователя")
    name = models.CharField(max_length=30, null=False,
                            blank=False, verbose_name="Имя пользователя")
    phone_number = models.CharField(
        max_length=9, null=True, blank=False, verbose_name="Телефон")
    username = models.CharField(
        max_length=20, null=True, blank=False, verbose_name="Юзернейм в телеграме")
    joined_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    notifications = models.BooleanField(
        default=True, verbose_name="Подписка на уведомления")

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
    description = models.TextField(
        verbose_name="Описание", max_length=1024)
    price = models.PositiveBigIntegerField(
        verbose_name="Цена", null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория", null=True)
    image_1 = models.ImageField(
        "Фото 1", upload_to="uploads/products/%Y_%m_%d/", null=True)
    image_2 = models.ImageField(
        "Фото 2", upload_to="uploads/products/%Y_%m_%d/", null=True)
    image_3 = models.ImageField(
        "Фото 3", upload_to="uploads/products/%Y_%m_%d/", null=True)
    image_4 = models.ImageField(
        "Фото 4", upload_to="uploads/products/%Y_%m_%d/", null=True)
    image_5 = models.ImageField(
        "Фото 5", upload_to="uploads/products/%Y_%m_%d/", null=True)
    image_6 = models.ImageField(
        "Фото 6", upload_to="uploads/products/%Y_%m_%d/", null=True)
    image_7 = models.ImageField(
        "Фото 7", upload_to="uploads/products/%Y_%m_%d/", null=True)
    image_8 = models.ImageField(
        "Фото 8", upload_to="uploads/products/%Y_%m_%d/", null=True)
    image_9 = models.ImageField(
        "Фото 9", upload_to="uploads/products/%Y_%m_%d/", null=True)
    image_10 = models.ImageField(
        "Фото 10", upload_to="uploads/products/%Y_%m_%d/", null=True)

    class Meta:
        verbose_name_plural = "Продукты"
        verbose_name = "Продукт"

    def __str__(self):
        return self.name


class Promo(models.Model):

    name = models.CharField(max_length=255, null=True,
                            blank=False, verbose_name="Название промо-акции")
    text = models.TextField(verbose_name="Текст",
                            max_length=1024)
    image = models.ImageField(
        "Фото", upload_to="uploads/promo/%Y_%m_%d")

    date_published = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Промоакция"
        verbose_name_plural = "Промокации"

    def __str__(self):
        return self.name

from rest_framework import serializers
from telegram_bot.models import User, Category, Product, Promo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PromoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promo
        fields = '__all__'

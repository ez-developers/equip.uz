from telegram_bot.models import User, Category, Product
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import UserSerializer, CategorySerializer, ProductSerializer
from django.http import Http404, HttpResponse
from django.core import serializers
from rest_framework.views import APIView
from rest_framework import generics


@permission_classes([IsAuthenticated])
class productsList(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')


@permission_classes([IsAuthenticated])
class ProductsListView(APIView):
    """
    A view that returns the count of active users in JSON.
    """

    def get(self, request, format=None):
        products = Product.objects.all()
        data = serializers.serialize('json', products)
        return HttpResponse(data, content_type="application/json")


@permission_classes([IsAuthenticated])
class productDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@permission_classes([IsAuthenticated])
class usersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes([IsAuthenticated])
class userDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes([IsAuthenticated])
class categoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@permission_classes([IsAuthenticated])
class categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

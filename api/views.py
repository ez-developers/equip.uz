from telegram_bot.models import User, Category, Product
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import UserSerializer, CategorySerializer, ProductSerializer

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getUser(request, pk):
    user = User.objects.get(user_id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getProducts(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)    

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getProduct(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

    


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getCategory(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)




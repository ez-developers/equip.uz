from telegram_bot.models import User, Category, Product, Promo
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, PromoSerializer
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework import generics


@permission_classes([IsAuthenticated])
class productsList(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')


@permission_classes([IsAuthenticated])
class usersList(APIView):

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')


@permission_classes([IsAuthenticated])
class userAdd(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class userDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes([IsAuthenticated])
class categoriesList(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)

        return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')


@permission_classes([IsAuthenticated])
class promoList(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Promo.objects.all()
        serializer = PromoSerializer(queryset, many=True)

        return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def promoDetail(request, pk):
    m = Promo.objects.get(pk=pk)
    serializer = PromoSerializer(m)
    return Response(serializer.data, status=status.HTTP_200_OK)

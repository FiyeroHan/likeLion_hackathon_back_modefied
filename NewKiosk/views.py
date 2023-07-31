from django.shortcuts import render
from rest_framework.response import Response


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Category, Product, Order, Product_Order
from .serializers import OrderSerializer, ProductSerializer, CategorySerializer, Product_OrderSerializer, MenuSerializer

class MenuApiView(APIView):
    def get(self, request):
        return
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class Product_OrderViewSet(viewsets.ModelViewSet):
    queryset = Product_Order.objects.all()
    serializer_class = OrderSerializer

class TestApiView(APIView):
    def get(self, request):
        떡볶이류 = Product.objects.filter(category=1 )
        사이드류 = Product.objects.filter(category=2 )
        세트메뉴 = Product.objects.filter(category=3 )
        serializer = ProductSerializer(떡볶이류, 사이드류, 세트메뉴,many=True)
        return Response(serializer.data)
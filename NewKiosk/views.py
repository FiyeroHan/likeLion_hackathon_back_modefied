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
        queryset = Product.objects.filter(category=1, category=2, category=3)
        #사이드류 = Product.objects.filter( )
        #세트메뉴 = Product.objects.filter( )
        serializer = ProductSerializer(queryset ,many=True)
        return Response(serializer.data)
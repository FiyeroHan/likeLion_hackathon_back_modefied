from django.shortcuts import render
from rest_framework.response import Response


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Category, Product, Order, Product_Order
from .serializers import OrderSerializer, ProductSerializer, CategorySerializer, Product_OrderSerializer

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
        ttuk = Product.objects.filter(category=1)
        side = Product.objects.filter(category=2)
        sets = Product.objects.filter(category=3)

        ts = ProductSerializer(ttuk, many=True)
        ss = ProductSerializer(side, many=True)
        ses = ProductSerializer(sets, many=True)

        response = {
            "떡볶이류" : ts.data,
            "사이드" : ss.data,
            "세트" : ses.data
        }

        return Response(data=response)
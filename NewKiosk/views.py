from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Category, Product, Order, Product_Order
from .serializers import OrderSerializer, ProductSerializer, CategorySerializer, Product_OrderSerializer

    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderApiView(APIView):
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Product_OrderViewSet(viewsets.ModelViewSet):
    queryset = Product_Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            order_number = serializer.instance.order_number  # 주문번호
            return Response({"order_number": order_number}, status=status.HTTP_201_CREATED)
            #주문 성공시 주문번호 반환
        else:
            return Response({"result": "주문 접수가 실패하였습니다"}, status=status.HTTP_400_BAD_REQUEST)
            
class MenuApiView(APIView):
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


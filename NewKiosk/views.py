from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Category, Product, Order, Product_Order, Receipt
from .serializers import OrderSerializer, ProductSerializer, CategorySerializer, Product_OrderSerializer, ReceiptSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


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
# order 만들고 등록 후 DB에서 order_id를 가져와서


class Product_OrderAPIView(APIView):
    def get(self, request):
        queryset = Product_Order.objects.all()
        serializer = Product_OrderSerializer(queryset)
        if serializer.is_valid():
            serializer.save()
            order_number = serializer.instance.id  # 주문번호
            return Response({"order_number": order_number})
        return Response({"result": "주문 접수가 실패하였습니다"})

    def post(self, request):
        serializer = Product_OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Product_OrderViewSet(viewsets.ModelViewSet):
    queryset = Product_Order.objects.all()
    serializer_class = Product_OrderSerializer


'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print("=== ProductOrderForm ===", args, kwargs, kwargs["request"])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            order_number = serializer.instance.id  # 주문번호
            return Response({"order_number": order_number}, status=status.HTTP_201_CREATED)
            #주문 성공시 주문번호 반환
        else:
            return Response({"result": "주문 접수가 실패하였습니다"}, status=status.HTTP_400_BAD_REQUEST)
            '''


class MenuApiView(APIView):
    def get(self, request):
        ttuk = Product.objects.filter(category=1)
        side = Product.objects.filter(category=2)
        sets = Product.objects.filter(category=3)

        ts = ProductSerializer(ttuk, many=True)
        ss = ProductSerializer(side, many=True)
        ses = ProductSerializer(sets, many=True)

        response = {
            "떡볶이류": ts.data,
            "사이드": ss.data,
            "세트": ses.data
        }

        return Response(data=response)

# 오더 만들고 오더 등록. 아이디 받아서 프로덕트에 등록.
# 새로운 product_order를 다시 만든다.
# 그 product_order를 다시 DB에 저장.


class Product_OrderApiView(APIView):
    #    def post(self, request):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print("=== ProductOrderForm ===", args, kwargs, kwargs["request"])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            order_number = serializer.instance.id  # 주문번호
            return Response({"order_number": order_number}, status=status.HTTP_201_CREATED)
            # 주문 성공시 주문번호 반환
        else:
            return Response({"result": "주문 접수가 실패하였습니다"}, status=status.HTTP_400_BAD_REQUEST)


class ReceiptApiView(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
    def get(self, request, order_id):
        queryset = Receipt.objects.all()
        serializer = ReceiptSerializer(queryset)
        if serializer.is_valid():
            #order_id = Order.objects.get(id=order_id)
            # order_number = serializer.instance.id  # 주문번호
            return Response(serializer.data)
        return Response(serializer.errors)

    def post(self, request,order_id):
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            order_id = Order.objects.get(id=order_id)
            return Response({"order_id": order_id})
        return Response({"result": "주문 접수가 실패하였습니다"})



class OrderDetailApiView(APIView):
    def get(self, request, id):
        order = Order.objects.filter(id=id)
        order_serializer = OrderSerializer(order)

        return Response(order_serializer.data)

    def post(self, request):
        order_serializer = OrderSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data)
        return Response(order_serializer.errors)

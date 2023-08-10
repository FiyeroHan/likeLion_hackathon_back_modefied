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
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        product_nums = []
        for product_num in serializer.initial_data["products"]:
            product_nums.append(product_num)


        
        if serializer.is_valid():
            serializer.save()  
        
        else:
            return Response({"result": "주문 접수가 실패하였습니다"}, status=status.HTTP_400_BAD_REQUEST)
            
        for product_num in product_nums:
            print(product_nums)
            print(product_num)
            response = {}
            response["order"] = serializer.instance.id
            response["product"] = product_num
            serializer2 = Product_OrderSerializer(data=response)
            if serializer2.is_valid():
                print("okaaaaay!")  
                serializer2.save()

        order_number = serializer.instance.id  # 주문번호
        return Response({"order_number": order_number}, status=status.HTTP_201_CREATED)
            #주문 성공시 주문번호 반환



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
            "떡볶이류" : ts.data,
            "사이드" : ss.data,
            "세트" : ses.data
        }

        return Response(data=response)
    
#오더 만들고 오더 등록. 아이디 받아서 프로덕트에 등록.
#새로운 product_order를 다시 만든다.
#그 product_order를 다시 DB에 저장.

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
            #주문 성공시 주문번호 반환
        else:
            return Response({"result": "주문 접수가 실패하였습니다"}, status=status.HTTP_400_BAD_REQUEST)
    

class OrderDetailApiView(APIView):
    def get(self, request, id):
        order = Order.objects.filter(id=id)
        order_serializer = OrderSerializer(order, many=True)
        
        return Response(order_serializer.data)

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Category, Product, Order, Product_Order, Receipt
from .serializers import OrderSerializer, ProductSerializer, CategorySerializer, Product_OrderSerializer, ReceiptSerializer, OrderReceiptSerializer, ProductReceiptSerializer

    
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
        products = []
        for product_num in serializer.initial_data["products"]:
            product_nums.append(product_num)
# 시리얼라이즈 데이터 접근 3가지: https://velog.io/@94incheon/DRF-Serializer-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%91%EA%B7%BC3%EA%B0%80%EC%A7%80

# Product_Order에 추가
        if serializer.is_valid():
            serializer.save()  
        
        else:
            return Response({"result": "주문 접수가 실패하였습니다"}, status=status.HTTP_400_BAD_REQUEST)
            
        for product_num in product_nums:
            response2 = {}
            response2["order"] = serializer.instance.id
            response2["product"] = product_num
            serializer2 = Product_OrderSerializer(data=response2)
            if serializer2.is_valid():
                serializer2.save()
                
        order_number = serializer.instance.id  # 주문번호
        return Response({"order_number": order_number}, status=status.HTTP_201_CREATED)
            #주문 성공시 주문번호 반환
'''            products.append(Product.objects.filter(id = product_num))
              
        product_serializer = ProductSerializer(products, many=True)
        
        order_serializer = {
            "주문 번호": serializer.data['id'],
            "결제 방식": serializer.data['payment'],
            "포장 여부" : serializer.data['is_takeout'],
            "총 금액" : serializer.data['total_price']
                        
        }

        response3 = {
            "주문정보" :order_serializer,
            "주문상품": product_serializer
        }
        
        print(response3)
        serializer3 = ReceiptSerializer(data=response3)
        if serializer3.is_valid():
            print("구우우웃")
            serializer3.save()
        else:
            print(serializer3.error_messages)
'''


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

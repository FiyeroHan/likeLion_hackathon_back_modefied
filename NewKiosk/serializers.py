from rest_framework import serializers
from .models import Category, Product, Order, Product_Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','payment','is_takeout','total_price')

class Product_OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_Order
        fields = ('product''payment', 'is_takeout', 'total_price')

'''
class Product_OrderDetailSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())  #Product모델의 id값 필드 참조 
    quantity = serializers.IntegerField()  # 상품 주문 수량 필드

    class Meta:
        model = Product_OrderDetail
        fields = ('id', 'quantity')
'''

'''
class TestSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ''
'''

# POST /api/product-order/

# 	{
# 	"products" : [
# 		{
# 			"id" : 1, #상품별 아이디
# 			"quantity" : 2 #상품주문갯수
# 		},
# 		{
# 			"id" : 2,
# 			"quantity" : 1
# 		},
# 		...
# 	],
# 	"payment": "카드",
#     "is_takeout": false,
#     "total_price": 5000,
# }


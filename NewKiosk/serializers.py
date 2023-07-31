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
        fields = '__all__', 'products'
#products 추가 
class Product_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Order
        fields = 'products', 'payment','is_takeout','total_price'

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
# 			"number" : 2 #상품주문갯수
# 		},
# 		...
# 	],
# 	"payment": "카드",
#     "is_takeout": false,
#     "total_price": 5000,
# }


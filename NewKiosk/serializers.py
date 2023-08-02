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
        fields = '__all__'

'''
class TestSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ''
'''
    

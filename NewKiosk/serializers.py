from rest_framework import serializers
from .models import Category, Product, Order, Product_Order, Receipt


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
        fields = '__all__'


class Product_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        #        depth = 1 #안의 값 참조할 때 저걸 사용해주면 된다.
        model = Product_Order
        fields = '__all__'


class ProductReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'product_detail', 'price', 'quantity')


class OrderReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'payment', 'is_takeout',
                  'total_price', 'products')

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)

        for product_data in products_data:
            Product_Order.objects.create(order=order, **product_data)

        Receipt.objects.create(order=order)

        return order


class ReceiptSerializer(serializers.ModelSerializer):

    order = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    class Meta:
        model = Receipt
        fields = ('id', 'order', 'products')

    def get_order(self, obj):
        order = {
            "id": obj.order.id,
            "payment": obj.order.payment,
            "is_takeout": obj.order.is_takeout,
            "total_price": obj.order.total_price,
        }
        return order

    def get_products(self, obj):
        # 동일한 order id를 가진 product_order를 가져오게끔 필터링
        products_order = Product_Order.objects.filter(order=obj.order.id)
        products = [{
            "id": product_order.product.id,
            "product_name": product_order.product.product_name,
            "product_detail": product_order.product.product_detail,
            "price": product_order.product.price,
            "is_soldout": product_order.product.is_soldout,
            "category": product_order.product.category.id,
            "quantity": product_order.quantity,
        } for product_order in products_order]
        return products


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

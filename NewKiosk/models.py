from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_detail = models.CharField(max_length=50, blank=True, default="")
    price = models.IntegerField(default=0)
    category = models.ForeignKey(
        'Category', related_name='product', on_delete=models.CASCADE)
    is_soldout = models.BooleanField(default=False)
#    related_order = models.ManyToManyField('Order', through='Product_Order', related_name= 'a_product')


class Order(models.Model):
    products = models.ManyToManyField(
        'Product', through='Product_Order', related_name='ordered')
    payment = models.CharField(max_length=50)
    is_takeout = models.BooleanField(default=True)
    total_price = models.IntegerField(default=0)


class Product_Order(models.Model):
    order = models.ForeignKey(
        'Order', related_name='product_order', on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(
        'Product', related_name='product_order', on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(default=0)


class Receipt(models.Model):
    product = models.ManyToManyField('Product', related_name='receipt')
    order = models.OneToOneField(
        'Order', related_name='receipt', on_delete=models.CASCADE, unique=True)


# class Product_OrderDetail(models.Model):
#    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
#    id = models.ForeignKey(Product, related_name='product_order_details', on_delete=models.CASCADE)
#    quantity = models.IntegerField(default=1)  # 상품 주문 수량

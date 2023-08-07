'''
from django.contrib import admin
from django.urls import path, include

from .views import CategoryViewSet,  ProductViewSet, OrderViewSet ,Product_OrderViewSet

from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('category', CategoryViewSet)
routers.register('product', ProductViewSet)
routers.register('order', OrderViewSet)
routers.register('product-order', Product_OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls)),
]
'''
from django.urls import path,include
from django.contrib import admin

from .views import CategoryViewSet,  ProductViewSet, OrderViewSet ,Product_OrderViewSet, MenuApiView, OrderDetailApiView, ReceiptViewSet

from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('category', CategoryViewSet)
routers.register('product', ProductViewSet)
routers.register('order', OrderViewSet)
routers.register('product-order', Product_OrderViewSet)
routers.register('receipt', ReceiptViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
    path('api/menu/', MenuApiView.as_view(), name='menu'),
#    path('api/order/<int:id>', OrderDetailApiView.as_view(), name='orderdetail'),
]

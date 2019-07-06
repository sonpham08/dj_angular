from rest_framework import routers
from django.urls import include, path
from .api import (
                    ProductViewSet, 
                    CategoryViewSet,
                    CoinViewSet,
                    FlashSaleViewSet,
                    DealedProductViewSet,
                    CartViewSet,
                    StaffViewSet,
                    BillViewSet,
                    CommentViewSet,
                )

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'coins', CoinViewSet)
router.register(r'flashsales', FlashSaleViewSet)
router.register(r'dealed', DealedProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'staffs', StaffViewSet)
router.register(r'bills', BillViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu.views import (
    CategoryViewSet, ProductViewSet,
    TableViewSet, OrderViewSet, OrderItemViewSet 
)
#  Creating router
router = DefaultRouter()

#  Submitting each viewset with address
router.register(r"catagories", CategoryViewSet)
router.register(r"products", ProductViewSet)
router.register(r"tables", TableViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"orderitems", OrderItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

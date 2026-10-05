from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu.views import (
    CategoryViewSet, ProductViewSet,
    TableViewSet, OrderViewSet, OrderItemViewSet 
)
from django.conf import settings
from django.conf.urls.static import static

#  Creating router
router = DefaultRouter()

#  Submitting each viewset with address
router.register(r"catagories", CategoryViewSet)
router.register(r"products", ProductViewSet)
router.register(r"tables", TableViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"orderitems", OrderItemViewSet)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


#  for taking tokens 
# curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d '{"username":"mina", "password"
# : "123"}
# 
# 
# for filternig with the token that we got 
# curl "http://127.0.0.1:8000/api/ers/?status=pending" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkxMjMzMzgwLCJpYXQiOjE3OTEyMzMwODAsImp0aSI6IjQyZTcxZDlmMGJmZDQ2NDc4MDMwM2Q5YmY2OGZkZDJkIiwidXNlcl9pZCI6IjEifQ.5TjTF9YSI8tFKzcVJc2U3no5hKJBN5Z-MT6_sf1I_aY" -H "Accept: application/json"
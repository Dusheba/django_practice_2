from django.urls import path
from order.views import OrderList, OrderCreate, OrderRetrieve, OrderDestroy

urlpatterns = [
    path('', OrderList.as_view(), OrderCreate.as_view()),
    path('<int:pk>', OrderRetrieve.as_view(), OrderDestroy.as_view()),
]

from django.urls import path
from v1.apps.v1_orders.views import OrderListCreateAPIView, OrderRetrieveDestroyAPIView

urlpatterns = [
    path('', OrderListCreateAPIView.as_view()),
    path('<int:pk>', OrderRetrieveDestroyAPIView.as_view()),
]

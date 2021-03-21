from django.urls import path
from order.views import OrderListCreateAPIView, OrderRetrieveDestroyAPIView

urlpatterns = [
    path('', OrderListCreateAPIView.as_view()),
    path('<int:pk>', OrderRetrieveDestroyAPIView.as_view()),
]

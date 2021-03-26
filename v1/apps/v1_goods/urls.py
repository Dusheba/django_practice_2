from django.urls import path
from v1.apps.v1_goods.views import GoodViewSet

urlpatterns = [
    path('', GoodViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>', GoodViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
]

from django.urls import include, re_path

from v1.apps.v1_goods import urls as g_urls
from v1.apps.v1_orders import urls as o_urls

urlpatterns = [
    re_path(r"^goods/", include(g_urls)),
    re_path(r"^orders/", include(o_urls)),
]

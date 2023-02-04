from django.contrib import admin
from hardware_store import views as store_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hardware_store/consignment', store_views.ConsignmentViewSet)
router.register(r'hardware_store/goods', store_views.GoodsViewSet)
router.register(r'hardware_store/producer', store_views.ProducerViewSet)
router.register(r'hardware_store/department', store_views.DepartmentViewSet)
router.register(r'hardware_store/saleslog', store_views.SalesLogViewSet)
router.register(r'hardware_store/orders', store_views.OrdersViewSet)
router.register(r'hardware_store/order_item', store_views.OrdersItemViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path(r'hardware_store/filtred_goods/', store_views.GoodsSearchViewSet.as_view(), name='goods'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstadoPedidoViewSet, PedidoViewSet, DetallePedidoViewSet

router = DefaultRouter()
router.register(r'estados', EstadoPedidoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles', DetallePedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
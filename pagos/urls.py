from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MetodoPagoViewSet, PagoViewSet

router = DefaultRouter()
router.register(r'metodos', MetodoPagoViewSet)
router.register(r'pagos', PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TipoUserViewSet, LlaveSeguridadViewSet,
    SuperUserViewSet, AdminViewSet, SupervisorViewSet
)

router = DefaultRouter()
router.register(r'tipos', TipoUserViewSet)
router.register(r'llaves', LlaveSeguridadViewSet)
router.register(r'superusuarios', SuperUserViewSet)
router.register(r'administradores', AdminViewSet)
router.register(r'supervisores', SupervisorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerfilUsuarioViewSet

router = DefaultRouter()
router.register(r'perfiles', PerfilUsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
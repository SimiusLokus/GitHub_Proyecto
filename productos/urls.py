from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaViewSet,
    TallaViewSet,
    MarcaViewSet,
    ColorViewSet,
    MaterialViewSet,
    EstadoViewSet,
    PublicacionViewSet
)

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'tallas', TallaViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'colores', ColorViewSet)
router.register(r'materiales', MaterialViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'publicaciones', PublicacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from .views import MenuPrincipalView, PublicacionesView, UsuariosView, PedidosView

urlpatterns = [
    path("menu/", MenuPrincipalView.as_view()),
    path("menu/publicaciones/", PublicacionesView.as_view()),
    path("menu/usuarios/", UsuariosView.as_view()),
    path("menu/pedidos/", PedidosView.as_view()),
]
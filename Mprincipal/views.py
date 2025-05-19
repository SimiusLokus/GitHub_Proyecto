from rest_framework.views import APIView
from rest_framework.response import Response
from .services import obtener_publicaciones, obtener_usuarios, obtener_pedidos

class MenuPrincipalView(APIView):
    def get(self, request):
        return Response({
            "secciones": [
                {"nombre": "Publicaciones", "endpoint": "/menu/publicaciones/"},
                {"nombre": "Usuarios", "endpoint": "/menu/usuarios/"},
                {"nombre": "Pedidos", "endpoint": "/menu/pedidos/"},
            ]
        })

class PublicacionesView(APIView):
    def get(self, request):
        data = obtener_publicaciones()
        return Response(data)

class UsuariosView(APIView):
    def get(self, request):
        data = obtener_usuarios()
        return Response(data)

class PedidosView(APIView):
    def get(self, request):
        data = obtener_pedidos()
        return Response(data)
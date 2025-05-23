from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Publicacion
from .serializers import PublicacionSerializer

class PublicacionListView(APIView):
    def get(self, request):
        publicaciones = Publicacion.objects.all()

        # Filtros por precio
        try:
            precio_min = request.query_params.get('min')
            precio_max = request.query_params.get('max')
            if precio_min:
                publicaciones = publicaciones.filter(precio__gte=float(precio_min))
            if precio_max:
                publicaciones = publicaciones.filter(precio__lte=float(precio_max))
        except ValueError:
            return Response({"error": "precio min o max no válido"}, status=400)

        # Filtros por relaciones (ID o nombre)
        filtros = {
            'categoria': ('categoria__cod_id', 'categoria__nombre'),
            'talla': ('talla__cod_id', 'talla__nombre'),
            'marca': ('marca__cod_id', 'marca__nombre'),
            'color': ('color__cod_id', 'color__nombre'),
            'material': ('material__cod_id', 'material__nombre'),
            'estado': ('estado__cod_id', 'estado__nombre'),
        }

        for param, (campo_id, campo_nombre) in filtros.items():
            valor = request.query_params.get(param)
            if valor:
                if valor.isdigit():
                    publicaciones = publicaciones.filter(**{campo_id: int(valor)})
                else:
                    publicaciones = publicaciones.filter(**{campo_nombre + '__icontains': valor.strip()})

        # Búsqueda por nombre o descripción
        termino = request.query_params.get('buscar')
        if termino:
            publicaciones = publicaciones.filter(
                nombre__icontains=termino.strip()
            ) | publicaciones.filter(
                descripcion__icontains=termino.strip()
            )

        serializer = PublicacionSerializer(publicaciones.distinct(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PublicacionDetailView(APIView):
    def put(self, request, pk):
        publicacion = get_object_or_404(Publicacion, cod_id=pk)
        serializer = PublicacionSerializer(publicacion, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
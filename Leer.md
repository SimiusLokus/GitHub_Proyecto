Fecha: 16 de mayo de 2025
Proyecto: ProyectoPGH

1.- Estructura del modelo de datos
Se diseñó y creó una estructura escalable y normalizada para representar publicaciones de productos (prendas de segunda mano), donde cada atributo clave se modeló como entidad independiente con su propia tabla:

Modelos creados con cod_id como clave primaria autoincremental:

Categoria-Talla-Marca-Color-Material-Estado

[Modelo principal]

==Publicacion==

    contiene los atributos [nombre, descripcion, precio, fecha_publicacion, disponible, imagen]  llaves foráneas hacia los modelos anteriores.



[Vistas y rutas]

- Se implementaron ViewSets para cada modelo
- Operaciones CRUD automáticamente.

Se registraron todas las rutas en un router DRF, agrupadas dentro del archivo productos/urls.py.

Se configuró una redirección automática desde la URL raíz (/) hacia la lista de publicaciones:
=== http://127.0.0.1:8000/api/productos/publicaciones/ ===


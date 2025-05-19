import requests

BASE_URL = "http://localhost:8001"

def obtener_publicaciones():
    try:
        res = requests.get(f"{BASE_URL}/productos/publicaciones/")
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def obtener_usuarios():
    try:
        res = requests.get(f"{BASE_URL}/usuarios/perfiles")
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def obtener_pedidos():
    try:
        res = requests.get(f"{BASE_URL}/pedidos/pedidos",f"{BASE_URL}/pedidos/detalles")
       # res = requests.get(f"{BASE_URL}/pedidos/detalles")
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}
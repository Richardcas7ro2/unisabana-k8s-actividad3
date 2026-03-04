from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import socket
import os
import platform

app = FastAPI(title="K8S Demo API", version="1.0.0")

# Intentamos configurar la carpeta de templates relativa a este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

def get_ip_address():
    """Obtiene la dirección IP primaria de este pod/host."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Conecta a un servidor externo falso para obtener la IP por defecto de la interfaz
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Ruta raíz. Renderiza una plantilla web atractiva que muestra la
    información del host / pod desde el cual se está sirviendo.
    """
    hostname = os.getenv("HOSTNAME", socket.gethostname())
    k8s_node = os.getenv("NODE_NAME", "Local / Unknown Node")
    k8s_pod_ip = os.getenv("MY_POD_IP", get_ip_address())
    app_version = os.getenv("APP_VERSION", "v1.0.0 (Default)")
    color_theme = os.getenv("COLOR_THEME", "blue") # Para demostrar overrides de Helm!

    # Información adicional
    system_info = f"{platform.system()} {platform.release()}"

    context = {
        "request": request,
        "hostname": hostname,
        "ip_address": k8s_pod_ip,
        "node_name": k8s_node,
        "version": app_version,
        "theme": color_theme,
        "system": system_info
    }

    return templates.TemplateResponse("index.html", context)

@app.get("/health")
async def health_check():
    """Endpoint de salud para las asadas (Probes) de Kubernetes."""
    return {"status": "ok"}

@app.get("/api/info")
async def api_info():
    """Endpoint JSON puro por si se desea usar como API."""
    return {
        "hostname": os.getenv("HOSTNAME", socket.gethostname()),
        "ip": get_ip_address(),
        "version": os.getenv("APP_VERSION", "v1.0")
    }

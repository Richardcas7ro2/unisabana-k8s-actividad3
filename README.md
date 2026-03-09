# Actividad 3 - Despliegue Automatizado con Kubernetes y CI/CD (GitOps)

Este repositorio contiene la solución completa a la Actividad 3 de la maestría, enfocada en la creación, contenedorización y despliegue completamente automatizado de un microservicio utilizando principios modernos de DevOps y GitOps.

## 🚀 Arquitectura del Proyecto

El proyecto está compuesto por las siguientes piezas tecnológicas trabajando en conjunto:

1. **Microservicio Base (Python + FastAPI):** Una API ligera que sirve un frontend dinámico (HTML/CSS) renderizado con Jinja2. La aplicación es consciente de su entorno en Kubernetes y muestra metadata en tiempo real (IP del Pod, Hostname, Nodo, Tema, Versión).
2. **Contenedorización (Docker):** El microservicio está empaquetado en una imagen de Docker usando `python:3.11-slim`, garantizando portabilidad y seguridad al correr sin privilegios root.
3. **Infraestructura como Código (Helm):** Toda la infraestructura de Kubernetes (`Deployment`, `Service`, `Ingress`, variables de entorno) está parametrizada usando plantillas de Helm, permitiendo despliegues escalables y multi-entorno sin duplicar código.
4. **Clúster Local (KIND):** Kubernetes in Docker (KIND) se utiliza para emular un entorno real de clúster distribuido (1 Control Plane, 2 Workers) con un NGINX Ingress Controller.
5. **Integración Continua (GitHub Actions):** Un pipeline de CI configurado para reaccionar a cambios en el código base, construir automáticamente la nueva imagen Docker, subirla a Docker Hub y autorregistrar el nuevo tag de versión en el repositorio.
6. **Entrega Continua (ArgoCD):** Aplicación de la filosofía GitOps pura. ArgoCD vive dentro del clúster KIND y sincroniza automáticamente cualquier cambio detectado en este repositorio de GitHub (fuente de verdad) hacia los nodos de Kubernetes, logrando un flujo *Zero-Touch*.

## 📂 Estructura del Repositorio

- `/app/`: Contiene el código fuente del microservicio en Python (FastAPI).
- `/app/templates/`: Contiene la interfaz gráfica en HTML/CSS (Glassmorphism).
- `/helm/unisabanak8s/`: Contiene el Chart de Helm maestro con las plantillas de Kubernetes.
- `/.github/workflows/`: Contiene la definición del pipeline automatizado de CI/CD.
- `Dockerfile`: Instrucciones de construcción de la imagen.
- `kind-config.yaml`: Configuración del clúster local distribuido.
- `argocd/application.yaml`: Manifiesto declarativo que conecta ArgoCD con este repositorio.

## 🎥 Video de Demostración y Sustentación

En el siguiente enlace se encuentra el video detallando paso a paso el funcionamiento integral del sistema, demostrando cómo un simple cambio de código (Git Push) desencadena la construcción en la nube y la auto-actualización del clúster en tiempo real gracias a ArgoCD:

> **[📝 INSERTAR AQUÍ EL ENLACE AL VIDEO DE YOUTUBE / DRIVE]**

## ⚙️ Requisitos para Ejecución Local

Para reproducir este entorno de principio a fin, se requiere:
- Docker Desktop.
- KIND (Kubernetes in Docker).
- `kubectl` y `helm` instalados.
- NGINX Ingress Controller (versión para KIND).
- ArgoCD instalado en el clúster.

## 👨‍💻 Autores Grupo 11
Abdul Mauricio Reyes Parra.
Wilmer Ricardo Castro Delgadillo.
Daniel Alexander Rodriguez.
Manuel Ovalle Diaz.

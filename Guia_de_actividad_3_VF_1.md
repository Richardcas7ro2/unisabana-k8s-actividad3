# Guía de actividad 3

A continuación, le presentamos las orientaciones de las actividades de aprendizaje.

## Generalidades

- **Tiempo total previsto para el desarrollo de la actividad:** 4 horas.

### Indicadores de desempeño

- Diseñar arquitecturas de software utilizando estilos y patrones arquitectónicos reconocidos, asegurando que las soluciones propuestas sean escalables, mantenibles y alineadas con los requisitos técnicos y del negocio.

## Actividad: Trabajo K8S

### Descripción

El trabajo involucra la creación de microservicios individualmente desplegables, utilizando contenedores Docker, un orquestador de contenedores como Kubernetes y herramientas como Helm para la gestión de paquetes y configuraciones.

### Pasos

1. Trabaje con un microservicio básico. Diseñar los contenedores Docker para el microservicio incluyendo la configuración necesaria.
2. **Despliegue con Helm**
   - Crear charts de Helm el microservicio, especificando los valores y configuraciones necesarias.
   - Utilizar valores por defecto y overrides para personalizar las configuraciones según el entorno.
3. **Implementación de ArgoCD**
   - Desplegar ArgoCD en el clúster de Kubernetes.
   - Configurar repositorios Git como fuentes de definición de la aplicación.
   - Definir aplicación en ArgoCD para el microservicio, utilizando los charts de Helm.
4. **Automatización con Pipelines**
   - Cree los pipelines necesarios para desplegar el aplicativo en el momento de detectar un commit sobre la rama que configure, configurando pipelines de CI/CD para automatizar el proceso de construcción y despliegue del microservicio.

### Acá pondrá en práctica

- Docker
- Kubernetes
- Herramienta de CI que escoja
- ArgoCD
- Helm

## Entregables

- Código fuente que se usó
- Video presentando el resultado

## Recomendaciones para su entrega

- Recuerde que contará con fechas específicas para su desarrollo; le recomendamos organizar su tiempo con anterioridad y consultar las fechas habilitadas.
- Recuerde que esta es una actividad que se desarrolla desde el componente grupal o individual.

## Rúbrica de evaluación

### Criterio 1 (5 pts): Construcción y despliegue del microservicio (Docker/Helm/Kubernetes/ArgoCD)

| Nivel | Puntos | Descripción |
|---|---:|---|
| Excelente | 5 | El microservicio está completamente funcional, correctamente dockerizado, con charts de Helm bien estructurados y personalización de valores; el despliegue en Kubernetes y la integración con ArgoCD funcionan sin errores. |
| Bueno | 4 | El microservicio está funcional y correctamente dockerizado; los charts de Helm presentan configuraciones correctas, aunque con mejoras posibles; despliegue e integración con ArgoCD funcionan con mínimos ajustes requeridos. |
| Necesita mejorar | 3 | El microservicio funciona parcialmente; se identifican problemas menores en la configuración de Docker, Helm o ArgoCD que afectan el despliegue, pero son corregibles. |
| Deficiente | 2 | El microservicio no funciona completamente; existen errores significativos en Docker, Helm o ArgoCD que impiden el despliegue automatizado. |
| No cumple / no entrega | 0 | No se presenta un microservicio funcional ni configuración válida en Docker, Helm o ArgoCD. |

### Criterio 2 (5 pts): Pipelines CI/CD y entregables (código y video)

| Nivel | Puntos | Descripción |
|---|---:|---|
| Excelente | 5 | Los pipelines CI/CD están completamente automatizados, detectan commits correctamente y despliegan sin errores; el código está bien estructurado y el video explica claramente el resultado. |
| Bueno | 4 | Los pipelines están implementados y automatizan la mayoría de los procesos; el código es funcional y el video es claro, aunque con algunos detalles de mejora. |
| Necesita mejorar | 3 | Los pipelines funcionan parcialmente o requieren intervención manual; el código o el video presenta omisiones menores, pero son funcionales. |
| Deficiente | 2 | Los pipelines están incompletos o fallan frecuentemente; el código presenta errores graves o el video es insuficiente para mostrar el resultado. |
| No cumple / no entrega | 0 | No se implementan pipelines funcionales ni se entregan los materiales requeridos (código y video). |

### Criterio 3 (5 pts): Documentación, claridad del código y presentación en video

| Nivel | Puntos | Descripción |
|---|---:|---|
| Excelente | 5 | La documentación es clara, completa y bien estructurada; el código está debidamente comentado; el video es profesional y explica todo el flujo. |
| Bueno | 4 | La documentación cubre la mayoría de los aspectos; el código está ordenado con comentarios básicos; el video es claro y suficientemente detallado. |
| Necesita mejorar | 3 | La documentación es parcial o incompleta; el código carece de comentarios en partes clave; el video no cubre todos los aspectos del proyecto. |
| Deficiente | 2 | La documentación es mínima y confusa; el código es poco entendible; el video es superficial y carece de detalles relevantes. |
| No cumple / no entrega | 0 | No se presenta documentación y el código no tiene estructura ni comentarios. |

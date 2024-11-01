# API-DJANGO

Una API desarrollada con Django que utiliza MySQL como base de datos. Este proyecto estaba pensado para ser configurado para ejecutarse en contenedores Docker, facilitando la configuración y el despliegue, **pero no se logro usar dockerfile ni docker-compose.yml**

## Tabla de Contenidos

- [Arquitectura](#arquitectura)
- [Requisitos](#requisitos)
- [Configuración Inicial](#configuración-inicial)
- [Migraciones y Superusuario](#migraciones-y-superusuario)
- [Ejecución del Proyecto Local](#ejecución-del-proyecto-local)
- [Uso de la API](#uso-de-la-api)
- [Ejecución de Pruebas](#ejecución-de-pruebas)

## Arquitectura

Este proyecto utiliza una arquitectura basada en microservicios, lo cual permite modularizar la aplicación en componentes independientes y reutilizables. Gracias a la estructura de Django, cada funcionalidad puede organizarse en aplicaciones (apps) autónomas, que facilitan el desarrollo, mantenimiento y escalabilidad del proyecto. Esta organización permite que cada microservicio tenga responsabilidades específicas, lo cual optimiza la implementación de cambios y mejora la capacidad de escalar cada módulo de forma independiente.

- **Django**: Framework principal para construir la API REST y organizar la aplicación en microservicios mediante apps independientes.
- **MySQL**: Base de datos relacional.

### Estructura de Carpetas

- **api**: Contiene las aplicaciones de Django.
- **estaciones**: Configuración del proyecto Django (incluye `settings.py`).

## Requisitos

- Python 3.11
- MySQL 8.0
- pip

Además, las dependencias están listadas en `requirements.txt`.

## Configuración Inicial

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/API-DJANGO.git
   cd API-DJANGO
   ```
2. Crea un entorno virtual y actívalo:
   ```bash
   python3 -m venv venv
   venv\Scripts\activate
   ```
3. Instalar las dependencias.
   `pip install -r requirements.txt`

4. Crear base de datos local:

- Abre la terminal:
  `mysql -u root -p`

- Ejecuta el script: Con el comando `source`, puedes ejecutar el script completo para crear la base de datos `estaciones_SIATA` y seleccionarla.
  `source /ruta/a/db.sql;`
  _Nota: el archivo se encuentra en el respositorio_

4. Crea un archivo `.env` en la raíz del proyecto y agrega las variables de entorno requeridas.

- ejemplo:
  ```bash
  DB_NAME=estaciones_SIATA
  DB_USER=tu_usuario
  DB_PASSWORD=tu_contraseña
  DB_HOST=localhost
  DB_PORT=3306
  ```

## Migraciones y Superusuario

Para acceder al panel de administración de Django.

1. Aplica las migraciones:
   `python manage.py migrate`

2. Crea superusuario:
   `python manage.py createsuperuser`

Después de crear el superusuario, podrás acceder al panel de administración en http://localhost:8000/admin.

## Ejecución del Proyecto Local

Con el entorno virtual activado, ejecuta el servidor de desarrollo de Django:
`python manage.py runserver`

Accede a la aplicación en http://localhost:8000.

## Uso de la API

Esta API incluye tres endpoints básicos. A continuación, se muestran sus funcionalidades:

- `POST /api/v1/estaciones`: Crea una nueva estación. Este endpoint recibe un cuerpo de solicitud (body) con los datos necesarios para la estación, incluyendo nombre y ubicación. En respuesta, devuelve los datos de la estación recién creada.
  **Ejemplo**:
  ```bash
  {
  "nombre":"Estación principal",
  "ubicacion": [-23,45]
  }
  ```
- `GET /api/v1/estaciones`: Recupera la lista completa de todas las estaciones registradas.
- `GET /api/v1/cercanas/{id}`: Busca y devuelve la estación más cercana a la estación especificada por el ID proporcionado en la ruta.

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias en la aplicación
`python manage.py test`

Se llevaron a cabo dos pruebas unitarias clave para garantizar la funcionalidad básica del sistema:

1. **Creación de Estación**: Verifica que el sistema pueda crear correctamente una nueva estación con todos los parámetros necesarios.
2. **Búsqueda de Estación Cercana**: Evalúa que el sistema sea capaz de identificar correctamente la estación más cercana a una ubicación especificada.

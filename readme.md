# 🧪 Prueba Técnica Backend - Django + PostgreSQL

## 📝 Proyecto

Este es un proyecto backend desarrollado con Django y Django Rest Framework, diseñado para gestionar datos geoespaciales utilizando PostgreSQL con la extención PostGIS.


 ## 🚀 Características Principales

- **API REST:** Implementación de endpoints para manejar datos geoespaciales.
- **Geodatos:** Soporte para datos vectoriales a través de PostGIS.
- **Autenticación JWT:** Seguridad en los endpoints a través de JSON Web Tokens.
- **Contenerización:** Uso de Docker para un entorno de desarrollo consistente.

## 🛠️ Tecnologías Utilizadas

- Python 3.11
- Django 5.2.6
- Django Rest Framework
- PostgreSQL con PostGIS
- Docker
- GDAL

## 📂 Estructura de Carpetas del Proyecto

La estructura del proyecto sigue un enfoque modular, separando las aplicaciones personalizadas del código de configuración principal para garantizar una organización clara y escalable.

```
PRUEBAINGRESO_BACK/
├── .venv/                      
├── .gitignore                  
├── .env                        # Variables de entorno (privado)
├── manage.py                   
├── requirements.txt            
├── prueba_tecnica/             
│   ├── asgi.py
│   ├── urls.py                 
│   └── wsgi.py
├── apps/                       
│   ├── api/                    
│   │   ├── __pycache__/
│   │   ├── serializers/        
│   │   ├── urls.py             
│   │   └── views.py           
│   └── datos/                  
│       ├── __pycache__/
│       ├── municipios/
│       ├── oficinas/
│       └── migrations/
├── data/                       # Almacena archivos de datos externos, como los .shp
│   ├── municipios_shp/
│   └── puntos_oficiales_shp/
└── settings/                   # Configuración del proyecto por entorno
    ├── __init__.py
    ├── base.py                 # Configuración base común
    ├── dev.py                  # Configuración de desarrollo
    └── prod.py                 # Configuración de producción
```

## ⚙️ Configuración del Entorno de Desarrollo

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

**1. Requisitos previos**

Asegurate de tener instalados los siguientes programas:
- Docker Desktop o tener una cuenta en Docker.
- Python 3.11
- Git

**2. Colnar el repositorio**

Clona el repositorio desde GitHub:
> git clone https://github.com/JeidKata/pruebaingreso_back.git

**3. Configura el entorno**

Crea y activa un entorno virtual de Python:

```
   python -m venv .venv

   # En Windows:
   .venv\Scripts\activate

   # En macOS/Linux:
   source .venv/bin/activate
```

**4. Variables de entorno**

Crea un archivo ```.env``` en la raíz del proyecto y agrega las siguiente variables para la configuraciób de la base de datos y la clave secreta.

```
SECRET_KEY=tu_clave_secreta_aqui
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=mysecretpassword
DB_HOST=localhost
DB_PORT=5432
```
**5. Contenedor de la Base de Datos**

```
docker run --name <nombre_tu_contenedor> -e POSTGRES_PASSWORD=<mysecretpassword> -p 5432:5432 -d postgis/postgis
```
**6. Instalar dependencias**

Instala las bibliotecas de Python necesarias:

```
pip install -r requirements.txt
```

## 🚀 Uso y Ejecución del Proyector

**1. Migraciones de la Base de Datos**

Aplica las migraciones para crear las tablas necesarias.
```
pyhton manage.py migrate
```
**2. Creación de superusuario**

Crea un supersuario para poder acceder al panel de administración y usar los endpoints protegidos.
```
python manage.py createsuperuser
```
**3. Carga de datos Geoespaciales**

En la carpeta ```data/``` encontraras archivos ```.shp```, para cárgarlos en la base de datos debe usar ```shp2pgsql```.

Asegurate de que el contenedor de Docker esté en ejecución.
```
# Entrar al contenedor 
docker exec -it <tu_contenedor> bash

# Copia los archivos .shp, .shx, .dbf, y .prj al contenedor 
docker cp C:\tu\ruta\Municipios.shp <tu-contenedor>:/nombre_carpeta/

docker cp C:\tu\ruta\Municipios.shx <tu-contenedor>:/nombre_carpeta/

# Instala PostGIS (si no cargaste una imagen de postgreSQL con PostGIS)
   apt-get update
   apt-get install -y postgis postgresql-16-postgis-3

# Ejecuta dentro de la carpeta 
cd /nombre_carpeta

shp2pgsql -s 4326 -I Municipios.shp public.municipios | psql -h localhost -U postgres -d postgres

shp2pgsql -s 4326 -I puntos_oficinas.shp  public.oficinas | psql -h localhost -U postgres -d postgres
```
**4. Iniciar el servidor de desarrollo**

Ejecuta el servidor de Django.
```
python manage.py runserver
```
El servidor estará disponible en ```http://127.0.0.1:8000/```.

## 📌 Endpoints de la API

Los endpoints de tu API están protegidos y requieren autenticación JWT.

Obtener Tokens de Autenticación
Para obtener los tokens, realiza una solicitud POST a /api/token/ con tus credenciales de superusuario.

**1.** Lista de Municipios por Departamento
- URL: http://127.0.0.1:8000/api/municipios-por-departamento
- Método: GET
- Parámetros de consulta: departamento=<nombre_del_departamento>
- Autenticación: Token JWT requerido en el encabezado Authorization.

**2.** Geometría de un Municipio por Oficina
- URL: http://127.0.0.1:8000/api/geometria-municipio-por-oficina/<int:oficina_id>/
- Método: GET
- Autenticación: Token JWT requerido en el encabezado Authorization.

---
<div align="center">
⭐ **¡No olvides dar una estrella al repositorio si te fue útil!** ⭐

[![Made with ❤️ by Jeidy Olaya](https://img.shields.io/badge/Made%20with%20⭐%20by-Jeidy%20Olaya-red.svg)](https://github.com/JeidKata)
</div>

# Proyecto Django: Información de Estaciones de Bicicletas y Buscador de Proyectos

Este proyecto utiliza Django para crear dos tareas que obtienen información de diferentes APIs y la guardan en una base de datos SQLite. Además, se muestran los datos en una tabla en una de las vistas del proyecto.

## Instrucciones de ejecución
Para ejecutar este proyecto en tu computadora, sigue los siguientes pasos:

1. Clona el repositorio en tu máquina local:

  ``git clone https://github.com/TU_USUARIO/nombre-del-repositorio.git``



2. Abre una terminal en el directorio raíz del proyecto.

3. Instala los paquetes necesarios utilizando pip:


  ``pip install -r requirements.txt``

4. Ejecuta las migraciones para crear las tablas de la base de datos:

  ``python manage.py migrate``
  
5. Ejecuta el servidor de desarrollo de Django:

``python manage.py runserver``

6. Visita <http://localhost:8000/users/> en tu navegador para ver la tabla de información de las estaciones de bicicletas o <http://localhost:8000/proyectos/> para ver la tabla de información de los proyectos.
### Librerías utilizadas
#### Este proyecto utiliza las siguientes librerías de Python:

- Django: framework web utilizado para desarrollar el proyecto.
- Requests: librería utilizada para hacer peticiones HTTP a las APIs.
- Beautiful Soup 4: librería utilizada para analizar el HTML de las páginas web de los proyectos.
- json: librería utilizada para guardar la información de los proyectos en un archivo JSON.
- django-paginator: librería utilizada para paginar los resultados de las estaciones de bicicletas en la tabla.
- 

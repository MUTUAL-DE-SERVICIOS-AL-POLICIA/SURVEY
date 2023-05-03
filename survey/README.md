instalar python 
crear un entorno virtual para la instalacion de paquetes necesarios para la aplicacion
- mkdir entornos
- cd entornos
- virtualenv rest --python=python3
activamos el entorno virtual
- source rest/bin/activate
instalamos django y djangorestframework dentro del entorno virtual
- pip3 install django
- pip3 install djangorestframework
Nos dirijimos a la carpeta donde se clono el proyecto
creamos las migraciones
- python3 manage.py makemigration
creamos las tablas en la base de datos
- python3 manage.py migrate
# Requerimientos
* python
* pip para python3
```sh
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt-get install python3-pip
```
* virtual env
```sh
sudo pip3 install virtualenv
```
# Crear un entorno virtual para la instalacion de paquetes necesarios para la aplicacion
```sh
mkdir entornos
cd entornos
virtualenv rest --python=python3
```
# Activamos el entorno virtual
```sh
source rest/bin/activate
```
# Instalamos los librerias necesarias dentro del entorno virtual
```sh
pip install --upgrade pip
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install pillow
pip install psycopg2
pip install django-cors-headers
pip install djangorestframework-simplejwt

```
# Nos dirijimos a la carpeta donde se clono el proyecto
# Configuramos la conexion a la base de datos en el archivo settings.py de la carpeta survey
# creamos las migraciones
```sh
python3 manage.py makemigrations
```
# creamos las tablas en la base de datos
```sh
python3 manage.py migrate
```
# levantar los servicios
```sh
python3 manage.py runserver
```
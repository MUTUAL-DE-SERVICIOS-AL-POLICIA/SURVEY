# Requerimientos
* docker

# Construir imagen
```sh
docker build -t survey/docker-django .
```

# Ejecutar contenedor con su volumen
```sh
docker run -v -d /{directorio de la aplicación}/:/app -p 8000:8000 survey/docker-django
```

# listar contenedores
```sh
docker ps -a
```

# Ver logs
```sh
docker logs --follow <id_container>
```
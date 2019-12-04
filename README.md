# Curso Docker - KeepCoding

## 0. Inicio

## 1. Introducción

### 1.1 Introducción a Contenedores y Docker
- Industria software ha cambiado:
- Antes
    - App monolíticas.
    - Largos ciclos de desarollo.
    - Entorno único.
    - Escalado lentamente.
- Ahora
    - Servicios desacoplados.
    - Mejoras rápidas e iterativas.
    - Múltiples entornos.
    - Escalar rápidamente.
- Implementación se vuelve muy compleja
- Muchos conocimientos diferentes
    - Lenguajes
    - Frameworks
    - BBDD
- Muchos entornos diferentes
    - Entornos de desarroll individual.
    - Preproducción, QA, integración, etc.
    - Producción: cloud e hybrid.
- Docker es una herramienta de código abierto.
- Dos versiones: Community Edition (+ usada) y Enterprise Edition (+ estable y con soporte).
- Paquetizar todas las aplicaciones y poder usarlas en cualquier SO.
- Permite ensamblar apps rápidas y elimina problemas que pueden ocurrir al enviar el código pudiendo subir a producción de manera más rápida y eficaz.

### 1.2 Características
- **Ligero**: los contenedores de una máquina comparten el mismo Kernel. Esto no ocurre con las MVs.
- **Portable**: el proceso que se arranca con el sistema de ficheros lleva todas las dependencias para que la aplicación funcione en cualquier máquina a la que se porte.
- **Inmutable**: si funciona en el equipo de desarrollo, funcionará en todos los equipos donde se ejecute.
- Docker trabaja con un lema: **Build, ship and run any app, anywhere**. (Generar los contenedores, transportarlos y ejecutarlos)
- ¿Qué aporta?
    - Escalabilidad: horizontal (añadiendo nodos como sean necesarios) y vertical (portando el contenedor a una máquina con + recursos). 
    - Portabilidad

### 1.3 Componentes de Docker
- Arquitectura muy modular: muchos componentes, algunos de muy alto nivel, que permiten personalizar bastante Docker.
- Componentes principales:
    - **Cliente**
        - El usuario interactúa con el demonio por medio del cliente.
        - Suele utilizarse la línea de comandos.
        - Tiene API. Permite escribir programas que interactuen directamente con el demonio sin usar el cliente.
        - Se usa para hablar con el dominio a través del protocolo HTTP.
    - **Demonio**
        - Proceso principal de gestión del _engine_. 
        - Corre en la misma máquina anfitriona. No siempre tiene que estar instalado en la máquina, y como cliente nos podemos conectar al demonio y lanzar instrucciones. - Responsable de crear, ejecutar y monitorizar los contenedores. También de construir y almacenar las imágenes. 
        - Todas las instrucciones se lanzan contra este.
        - Acepta peticiones y crea imágenes.
    - **Registry**
        - Almacenan y distribuyen imágenes.
        - Predeterminado: Docker Hub. 

![Componentes principales](Images/1.3_componentes_01.png)

### 1.4 Concepto de contenedores
- **Contenedores**
    - Proceso aislado al resto de procesos del sistema. 
    - Paquete que contiene una app y todo el software necesario para que se ejecute.
    - Teniendo instalado Docker Engine se pueden ejecutar tantos contenedores como se desee.
    - Es ejecutado por el kernel del host, como una app más pero de forma aislada del resto ya que tiene su propio sistema de ficheros.
    - Dispone de su propio espacio de usuario (atributos, ids, grupos, etc).
    - Dispone de su propio espacio de procesos: provee opción de suspensión y recuperación de procesos en la misma máquina o al migrarse.
    - Se pueden compartir espacio de ficheros con la máquina host, o espacio de usuarios y procesos con otros contenedores.

![Concepto de contenedores](Images/1.4_concepto_contenedores_01.png)

### 1.5 Diferencia entre contenedores y máquinas virtuales
- Virtualización
    - Máquina virtual: virtualización del entorno de ejecución para ejecutar aplicaciones.
    - Virtualización del hardware
- El contenedor tiene lo escencial para ejecutar la aplicación. 
- Una MV tiene todo el SO y dentro de este se pueden instalar diferentes servicios, con el consiguiente consumo que supone.
- Entorno virtualizado
    - Varios SOs.
    - SO invitado. Es el que se ejecuta sobre el HW virtualizado. 
    - Ventajas
        - Ejecucción de un SO diferente al instalado.
        - Posibilidad de clonar y mover la MV de un ordenador físico a otro.
        - Aprovechamiento de recursos con varios _guests_ en un mismo host.
    - Inconvenientes
        - Rendimiento.
        - Nº de sistemas corriendo en la misma máquina.

![Máquinas virtuales vs contenedores](Images/1.5_diferencias_contenedores_vms_01.png)

![Máquinas virtuales vs contenedores II](Images/1.5_diferencias_contenedores_vms_02.png)

### 1.6 ¿Por qué son tan eficientes los contenedores?
- Un contenedor no necesita hipervisor.
- Un contenedor es un paquete. Contiene una aplicación y todo el sw necesario para ejecutarlo.
- El contenedor se ejecuta directamente por el kernel del host.

## 2. Instalación

### 2.1 Docker en los distintos sistemas operativos

![Docker en los distintos Sistemas Operativos](Images/2.1_docker_ssoo_01.png)

![Docker en los distintos Sistemas Operativos II](Images/2.1_docker_ssoo_02.png)

### 2.2 Instalar Docker en Linux
- Guía de instalación: https://docs.docker.com/install/
- Máquina virtual
    - **Usuario**: Ubuntu_1804
    - **Contraseña:** password
- Instalación (seguir web)
```bash
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce
```

- Probar funcionamiento
    - **Run** ejecuta el contenedor listado a continuación del comando.
```bash
sudo docker run hello-world
```

- Añadir al usuario para que no utilice sudo
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
### 2.3 Primer Contenedor
```bash
docker run hello-world
```

## 3. Empezando con Docker

### 3.1 Comandos Docker
- Docker asigna nombres aleatorios a los contenedores (si no le asignados uno antes).
- Ayuda
    - Están agrupados por funcionalidades.
```bash
$ docker help
$ docker COMMAND --help
$ docker container --help
$ docker container ls
$ docker container ls --help
$ docker rm zealous_golick
$ docker image --help
$ docker image ls -a
$ docker image rm hello-world -f
$ docker version
$ docker search ubuntu
```

### 3.2 Imágenes y contenedores
- **Imagen**
    - Conjunto de ficheros que contiene todos los elementos necesarios para que la imagen pueda ser ejecutada.
    - NO tienen estado.
    - NUNCA cambian, son fijas, siempre. NO se pueden modificar.
    - Cada vez que se ejecuta un **docker run** de una imagen, se genera un nuevo contenedor.
    - Se pueden ejecutar varios contenedores de la misma imagen.
    - "Plantilla base"
- **Contenedor**
    - Instancia en ejecución de una imagen.
    - SI tiene estados (arrancado, pausado, detenido o terminado) y se puede modificar (añadir ficheros, por ej).
    - Se puede modificar su contenido e información estando en ejecución.
    - "Ejecución de la plantilla".
- **Comandos**
    - Imágenes
        - **Pull**: bajar la imagen.
        - **Push**: se genera imagen y se sube.
        - **Build**: crear imágenes.
        - **Save**: guardar imagen.
        - **Load**: cargar imagen guardada.
    - Contenedores
        - **Run**
        - **Stop**
        - **Start**
        - **Restart**
        - **Inspect**
        - **Stats**

![Imágenes y contenedores](Images/3.2_imagenes_contenedores_01.png)

### 3.3 Docker Store - Docker Hub
- Las imágenes se descargan de:
    - Docker Store
    - Docker Hub

```bash
# Descarga una versión específica de Ubuntu
$ docker pull ubuntu:16.04 
```

### 3.4 Comandos para contenedores
```bash
$ docker ps -a # Se está deprecando, mejor usar ls

# Lista de directorio raíz todos los ficheros y directorios.
$ docker container run ubuntu ls -ltr 

# Lo mismo que el anterior pero de la versión anterior de UBuntu
$ docker container run ubuntu:16.04 ls -ltr

# Cambiar nombre (NAMES) por el que se escoja
$ docker container run --name miubuntu ubuntu:16.04 ls -ltr

# Ejecutar contenedor y dejarlo arrancado
$ docker container run --name ultimoubuntu ubuntu top -b

# Detener el contenedor que se está ejecutando
$ docker container stop 1506bd3b402b

# Ejecutar contenedor y dejarlo arrancado en segundo plano (detach)
$ docker container run -d --name ubu ubuntu top -b

# Ver logs que genera el contenedor
## Muestra los logs hasta el momento de ejecutar el comando
$ docker container logs --details 09af5050365f
## Muestra los logs en tiempo real (follow)
$ docker container logs -f 09af5050365f
```

### 3.5 Empezando con Docker - Ejercicio 1

### 3.6 Resumen

### 3.7 Comandos para imágenes

### 3.8 Empezando con Docker - Ejercicio 2

### 3.9 Empezando con Docker - Ejercicio 3

## 4. Creación de imágenes

## 5. Manejando volúmenes

## 6. Aplicaciones multicontenedor - Docker compose

## 7. Docker Registry

## 8. Trabajando con Docker en entornos de desarrollo

## 9. Kubernetes
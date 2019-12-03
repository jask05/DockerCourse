#Establecemos imagen base
FROM ubuntu:18.04
LABEL Author="Jose Luis Llorente" Desc="Descripcion" version="1.0"

COPY carpeta examples
COPY fichero.txt /examples

#Comando para indicar al contenedor que comando ejecutar cuando arranque
ENTRYPOINT cat /examples/fichero.txt


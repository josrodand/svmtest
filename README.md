# Control de versiones con Subversion

Repositorio de prueba para el uso de Subversion.
Subversion es un sistema de control de versiones centralizado, a diferencia de git, el cual es distribuido. Esta diferencia implica una serie de diferencias en cuanto a la gestión del código. Buscar en google para mas info.

Por supuesto al ser un sistema de control de versiones diferente y mas antiguo tiene un funcionamiento distinto.

# Instalacion

**Windows**
En windows hay que instalarse tortoiseSVN desde el siguiente link:
https://tortoisesvn.net/downloads.html

Esto instalará tanto el software con su propia GUI como el sistema svn que se emplea desde la powershell.

**Linux, MVs**
(en construccion)


# Funcionamiento de svn en pasos rapidos:

1. Elige un directorio para que sea tu repositorio local, el cual tendrá tu propia copia del repositorio remoto.

2. Carga/inicializa el repositorio local con una url de la nube.

```
svn checkout https://github.com/josrodand/svmtest.git
```
Una vez hecho esto ya tienes enganchado el remoto a tu local. No estoy seguro de si al hacerlo te actualiza lo que tengas, aunque si está vacio dara igual, en el caso por ejemplo que se haya creado un proyecto vacío en github.

3. Trabajo con el control de versiones

Hay una serie de comandos que s epueden usar para seguir el trabajo

- **svn status**: te dice si hay archivos cargados o eliminados para hacer un commit.
> NOTA: En subversion el commit es como commit + push en git.

- **svn_update**: Actualiza tu version local 

- **svn add archivo** pone en "stage" el archivo indicado, es decir, lo añade a la pila de cambios que se subiran al remoto 
- **svn delete archivo**
- 

Una vez añadidos todos los cambios se hace un commit, esto es, subir los cambios añadidos al repo. Generalmente se añade un mensaje descriptivo de los cambios.

```
svn commit -m "añadidos cambios"
```

Al ejecutar esas lineas, subversion actualizará el repositorio y le añadirá un nuevo numero de version.




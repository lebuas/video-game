
# Videojuego: Aviator

## Integrantes del Proyecto
- Leymar Buenaventura Asprilla
- Andrés Felipe Martinez Veloza

## Funcionalidad del Juego

### Descripción

Es un juego de acción y supervivencia en el que el jugador controla un avión que debe evitar que los enemigos lo alcancen, mientras destruye a otros aviones enemigos.

### Objetivo

El objetivo del juego es **alcanzar un mínimo de 20 positivos, en menos de un minuto** mientras evitas que los enemigos te alcancen.

### Reglas del Juego

- Tienes **5 vidas**.
- Mueve tu personaje utilizando las teclas de flecha **izquierda** y **derecha**.
- Dispara a los enemigos presionando la tecla **Espacio**.
- Si necesitas salir de la partida, presiona la tecla **'S'**.
- Evita que los enemigos te alcancen, ya que si tu vida llega a 0, perderás el juego.

## Para probar el juego, Seguir los siguientes paso:

## Clonar el Repositorio

Para clonar este repositorio, usa el siguiente comando en la terminal, navega hasta el directorio donde se desea clonar y luego ejecutamos el comando:

```bash
git https://github.com/lebuas/video-game.git
```
## Crear un entorno virtual
En la misma ruta donde se clono el repositorio, vamos a crear un entorno virtual con el siguiente comando:

En linux o entornos linux
```bash
python3 -m venv venv
```
En Windows:
```bash
python3 -m venv venv
```
## Activar entorno virtual
Vamos a activar el entorno virtual. En  el directorio donde se creo el entorno virtual, vamos a ingresar el siguiente comando:

En linux o entornos linux:
```bash
source venv/bin/activate
```
En windows:
```bash
source venv/Scripts/activate
```
## Instalar requerimiento del programa:

Una vez que el entorno virtual esté activo, instala las dependencias necesarias para el proyecto. Para ello, si tienes un archivo requirements.txt en el repositorio, simplemente ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```
Esperamos que se instalen

## Ejecutar la aplicación
Para ejecutar la aplicación, en la terminal, navegamos hasta el  directorio raiz donde clonamos el repositorio,abrimos una terminal desde esa ruta e ingresamos los siguientes comandos:


En linux o entornos linux:
```cd app/models/
```
Una vez en la ruta models ingresamos el siguientes comando par ejecutar el juego:

En linux o entornos linux:
```bash
 python3 main.py
```

Para windows:
```bash
 python main.py
```


## Documentos en la ruta:

```bash
cd /app/docs/
```

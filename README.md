# Repositorio Semana Tec

## Información general 

Este repositorio cuenta con el trabajo realizado en la Semana Tec "Herramientas Computacionales: el arte de la programación" TC1001S.1 

## Funcionamiento general
El proyecto realizado consiste en un programa desarrollado en Python que realiza procesamiento básico de una imagen, aplicando filtros/kernels a la misma, por medio de una convolución. 
Para probar el proyecto, se requieren 2 archivos: la libreria LIB.py, que contiene los kernels utilizados, y el archivo principal main.py, que utiliza los kernels para realizar la convolución de una imagen recibida como parámetro desde la línea de comandos.

##Estructura de código y commits a repositorio
Para realizar este proyecto, se siguieron los siguientes estándares: </br>
[Guía de estilo para Python](https://www.python.org/dev/peps/pep-0008/) </br>
[Guía de estilo para Git](https://medium.com/@nawarpianist/git-commit-best-practices-dab8d722de99)

## Procesamiento de imágenes

### Convolución
La convolución es el tratamiento que recibe una imagen, la cual en términos computacionales, es una matriz, por otra matriz "kernel". </br>
El kernel, o filtro, pasa por la primera matriz (la imagen original) y realiza multiplicaciones para aplicar el filtro deseado. 
Las convoluciones son útiles para las Convolutional Neural Networks (CNN), que se utilizan para realizar búsquedas dentro de las imágenes originales. [(Fuente)](https://wiki.pathmind.com/convolutional-network)

### Padding
A la hora de realizar convoluciones, se pueden perder píxeles en las orillas/bordes de la imagen, por lo que una buena práctica para no presentar pérdidas mientras más capas/kernels se aplican, es agregar un contorno/padding, incrementando el tamaño efectivo de la imagen, para no perder ningún píxel. [(fuente)](https://wiki.pathmind.com/convolutional-network)  

## Kernels utilizados 
### Sobel
Para detectar líneas y bordes en la imagen, se pueden utilizar kernels de Sobel, que funcionan de forma similar a los kernels de detección de bordes, pero con una optimización de suavización, que permite que no se vean tan afectados por el ruido.<br/>
Fuentes consultadas: [1](https://aishack.in/tutorials/image-convolution-examples/) y [2](https://setosa.io/ev/image-kernels/)
### Gauss blur
Utilizando la función para crear un kernel Gaussiano, logramos tener un kernel que nos permite crear una imagen con propiedades especiales para reconocimiento de computadoras. Se puede aproximar con una convolución de imagen<br/>
Fuentes consultadas: [1](https://aishack.in/tutorials/image-convolution-examples/) y [2](https://stackoverflow.com/questions/29731726/how-to-calculate-a-gaussian-kernel-matrix-efficiently-in-numpy)
### Laplace
Se implementaron dos funciones para crear un kernel de Laplace. Ambos kernel se usan para crear una imagen con bordes pronunciados. Debido a que es estado base, es muy sensible al ruido.<br/>
Fuentes consultadas: [1](https://aishack.in/tutorials/image-convolution-examples/) 
### Ricker Wavelet
El Ricker Wavelet, o "Mexican Hat", es la segunda derivada negativa normalizada de una función gaussiana. Normalmente se emplea para modelar datos sísmicos, y electrodinámica computacional. La generalización de esta es conocida como la "Laplacian of Gaussian". <br/>
Fuentes consultadas: [1](https://en.wikipedia.org/wiki/Ricker_wavelet) 
### Laplacian of Gaussian
Aplicamos la función para hacer un kernel de Laplace of Gaussian, el cual se utiliza para encontrar áreas de cambio rápido en las imágenes, esto debido a que los filtros derivados son muy sensibles al ruido, por lo tanto al suavizar una imagen antes de la función mejora los resultados.<br/>
Fuentes consultadas: [1](https://aishack.in/tutorials/image-convolution-examples/) y [2](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)

## Libreria
El archivo `LIB.py` contiene funciones para generar todos los kernels mencionados, recibiendo uno o más parámetros (dependiendo del kernel), los cuales son enviados desde el archivo main.py  </br>
Para el funcionamiento de la librería, se importa la librería de numpy, que se utiliza en la generación de matrices (kernels). </br>
El desarrollo de esta librería se dividió entre los integrantes del equipo de la siguiente forma:
- Funciones de Laplace realizadas por [Horacio Lamas](https://github.com/A01367213)
- Función de Laplacian of Gaussian realizada par [Myron Bean](https://github.com/myron57)
- Función de Gauss blur realizada por [Rubén Ruiz](https://github.com/redeyeruiz)
- Funciones de Sobel y Ricker Wavelet realizadas por [Victor Franco](https://github.com/v-franco)

## Archivo principal
El archivo `main.py` contiene una función principal llamada `imageProcessing` la cual realiza de:
- Procesamiento inicial de la imagen: Grayscale, conversión numérica y normalización 0-1
- Añadir un padding a la imagen procesada
- Generación de kernels (utilizando la librería local  `LIB.py`)
- Generación de la convolución de cada imagen, utilizando los kernels generados, y el método `convolve` de la clase `ndimage`, de la librería `scipy`
- Generación de una matriz 3x3 para desplegar los resultados de cada convolución, utilizando la librería `matplotlib.pyplot`
- Display de cada resultado en la matriz generada, con un título referente al kernel aplicado para la convolución

La función main() del archivo, recibe el nombre del archivo de imagen a utilizar, desde la línea de comandos. </br>
Para el funcionamiento del archivo, se utilizan las siguientes librerías:
- `matplotlib.pylot` para realizar el display de los resultados
- `numpy` para procesamiento inicial de imagen y generación de padding
- `argparse` para recibir el nombre del archivo a utilizar como argumento
- `PIL` para realizar manipulación de archivos tipo imagen. Se importa la clase `Image`
- `scipy` para realizar la convolución con cada kernel. Se importa la clase `ndimage`
- `LIB` para generar los kernels a utilizar. Librería local incluida en el archivo `LIB.py`

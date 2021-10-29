# Repositorio Semana Tec

## Información general 

Este repositorio cuenta con el trabajo realizado en la Semana Tec "Herramientas Computacionales: el arte de la programación" TC1001S.1 

##Funcionamiento general
El proyecto realizado consiste en un programa desarrollado en Python que realiza procesamiento básico de una imagen, aplicando filtros/kernels a la misma, por medio de una convolución. 

##Procesamiento de imágenes

###Convolución
La convolución es el tratamiento que recibe una imagen, la cual en términos computacionales, es una matriz, por otra matriz "kernel". </br>
El kernel, o filtro, pasa por la primera matriz (la imagen original) y realiza multiplicaciones para aplicar el filtro deseado. 
Las convoluciones son útiles para las Convolutional Neural Networks (CNN), que se utilizan para realizar búsquedas dentro de las imágenes originales. [(Fuente)](https://wiki.pathmind.com/convolutional-network)

###Padding
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

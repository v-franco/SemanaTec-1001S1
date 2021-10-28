# Repositorio Semana Tec

## Información general 

Este repositorio cuenta con el trabajo realizado en la Semana Tec "Herramientas Computacionales: el arte de la programación" TC1001S.1 

## Kernels utilizados 

### Gauss blur
Utilizando la función para crear un kernel Gaussiano, logramos tener un kernel que nos permite crear una imagen con propiedades especiales para reconocimiento de computadoras. Se puede aproximar con una convolución de imagen
Fuentes consultadas: [1](https://aishack.in/tutorials/image-convolution-examples/) y [2](https://stackoverflow.com/questions/29731726/how-to-calculate-a-gaussian-kernel-matrix-efficiently-in-numpy)
### Laplace
Se implementaron dos funciones para crear un kernel de Laplace. Ambos kernel se usan para crear una imagen con bordes pronunciados. Debido a que es estado base, es muy sensible al ruido.<br/>
Fuentes consultadas: [1](https://aishack.in/tutorials/image-convolution-examples/) 
### Laplace of Gaussian
Aplicamos la función para hacer un kernel de Laplace of Gaussian, el cual se utiliza para encontrar áreas de cambio rápido en las imágenes, esto debido a que los filtros derivados son muy sensibles al ruido, por lo tanto al suavizar una imagen antes de la función mejora los resultados.<br/>
Fuentes consultadas: [1](https://aishack.in/tutorials/image-convolution-examples/) y [2](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)
### Sobel
Para detectar líneas y bordes en la imagen, se pueden utilizar kernels de Sobel, que funcionan de forma similar a los kernels de detección de bordes, pero con una optimización de suavización, que permite que no se vean tan afectados por el ruido.<br/>
Fuentes consultadas: [1](https://aishack.in/tutorials/image-convolution-examples/) y [2](https://setosa.io/ev/image-kernels/)

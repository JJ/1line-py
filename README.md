# Python línea a línea

[![Build Status](https://travis-ci.org/JJ/1line-py.svg?branch=master)](https://travis-ci.org/JJ/1line-py)

## Cómpralo en Amazon

Compra
[aprende a programar en Python como si estuvieras en el siglo XXI: Pensamiento computacional a través de la programación funcional usando Python](http://amzn.to/2t1gKt7) por
menos de un euro. También [en tapa blanda](http://amzn.to/2sCZKu8) por
un precio bajísimo. 

## De qué va

Enseñando pensamiento computacional a partir de python
*one-liners*. Presentación con ejemplos [aquí](preso/). Es una
introducción muy básica, que no trata de cubrir ni todo el lenguaje ni
siquiera su sintaxis, sino su filosofía y cómo realizar diferentes
tareas de tratamiento de datos usándolo. Los ejemplos también comparan
Python con otros lenguajes, permitiendo ver también cómo la sintaxis
de unos y otros converge o diverge. 

## Una estructura (que seguramente cambiará)

1. [Para empezar a trabajar](txt/01.empezar.md).
2. [Tipos de datos básicos y cómo trabajar con ellos.](txt/02.datos.md)
3. [Lógica e ilógica](txt/03.logica.md).
4. [Datos menos simples](txt/04.componiendo.md)
5. [Almacenando valores](txt/05.identificando.md)
6. [Lo que el lenguaje no da](txt/06.sinpilas.md)

## Sugerencias y correcciones

Por lo pronto, no hay suficientes como para crear una plantilla. Tú
haz el *pull request* y será aceptado si es una corrección con una
alta probabilidad; si es un añadido tendrá que ser coherente con el
resto del texto, en estilo y en progresión. Por supuesto que
respetando la licencia de más abajo eres muy libre de añadir ese texto
y seguir trabajando con él.

## Agradecimientos

A [Manu](https://github.com/Makova) por
correcciones y a [José Manuel Colella](https://github.com/josecolella)
por varias aportaciones.
A [Jesús Leganés](https://github.com/piranna) por
consejos y revisiones,
a [Gregorio Robles](https://github.com/gregoriorobles) por una extensa
revisión y consejos para transformar este material en una clase. 

## Para generar el libro

Necesitarás tener instalado [pandoc](http://pandoc.org), LaTeX y las tipografías
usadas para que funcionen los scripts.

Para instalar todas las dependencias en Ubuntu 16.04:

```
sudo apt install pandoc texlive-xetex lmodern texlive-fonts-recommended
```

```
cd txt
../md2pdf   # PDF
../md2docx  # Procesador de textos
../md2epub  # ePub
```

## Si necesitas ayuda

Únete
al
[grupo de Telegram](https://t.me/joinchat/AOR8MglinRI4Jzk8cUwFdA) para
plantear dudas sobre los ejercicios del libro y sobre Python en
general, o para hacer sugerencias o señalar errores.

## Licencia

![cc-by-sa](https://i.creativecommons.org/l/by-sa/3.0/es/88x31.png)

Este libro tiene
licencia
[`cc-by-sa`](https://creativecommons.org/licenses/by-sa/3.0/es/), y el
código incluido en él [GPL](LICENSE).

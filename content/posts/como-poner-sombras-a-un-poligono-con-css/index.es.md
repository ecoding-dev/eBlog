---
title: "Como poner sombras a un poligono con CSS"
date: "2023-03-08 02:12:47"
lastmod: "2023-03-08 02:12:47"
draft: false
authors: ['Arnaldo']
description: "Guía de como poder establecer sombras a polígonos"
featuredImage: ""
tags: []
categories: ['Git']
---
# Como poner sombras a un poligono con CSS

_ <p>Guía de como poder establecer sombras a polígonos</p> _

__hace 3 años -___412 visitas_

Para poder ponerle sombras a un polígono tenemos que crear dos contenedores,
un contenedor padre que será el `shadow` y su contenedor hijo que será el
`polygon`.

    
    
    <div class="shadow">
        <div class="polygon"></div>
    </div>

En el contenedor `shadow` se define el color y rango de la sombra con la
propiedad `filter` y la función `drop-shadow()`. La función acepta un
parámetro de tipo (definido en la propiedad box-shadow).

    
    
    .shadow{
        filter: drop-shadow(0 0 1rem #4fd5b0);
    }

En el contenedor `polygon` definiremos las dimensiones del polígono con la
propiedad `clip-path` y la función `polygon()`.

    
    
    .polygon{
        width: 10rem;
        height: 10rem;
        clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
        background: #43acbb;
    }

### `example:`


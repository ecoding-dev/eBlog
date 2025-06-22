---
title: "Especificar directorio raíz para el uso mas cómodo de importaciones de módulos javascript en Visual Code"
date: "2022-03-17 10:36:46"
lastmod: "2022-03-17 10:36:46"
draft: false
authors: ['Abel']
description: "Cambiar importaciones “../../carpeta/modulo.js” a “carpeta/modulo.js”"
featuredImage: "https://ecoding.tech/storage/images/dpWSmlfNnn0gISMXbQ2RlGyJYUCzTloCpdtqUgqq.jpg"
tags: ['PHP', 'Laravel', 'Controller', 'Backend', 'Auth']
categories: ['Laravel']
---
# Especificar directorio raíz para el uso mas cómodo de importaciones de
módulos javascript en Visual Code

_ <p>Cambiar importaciones “../../carpeta/modulo.js” a “carpeta/modulo.js”</p>
_

__hace 3 años -___371 visitas_

Por defecto los archivos de JavaScript abiertos en Visual Studio Code se
tratan como unidades independientes. Siempre que un archivo a.js no haga
referencia a un archivo b.t explícitamente (ya sea usando importaciones de
módulos o CommonJS ), no hay un contexto de proyecto común entre los dos
archivos, por lo que las importaciones se harían de la siguiente manera.

![](https://ecoding.tech/storage/images/dpWSmlfNnn0gISMXbQ2RlGyJYUCzTloCpdtqUgqq.jpg)![](https://ecoding.tech/storage/images/JnJtPyVlEjCsdYRQJ3KKfVR8ZU1xXoRyY78nfetI.jpg)

Esto es algo incomodo, así que una solución sería crear un contexto único para
todos los archivos, creando un archivo llamado jsconfig.json en la carpeta
raíz del proyecto.

![](https://ecoding.tech/storage/images/9PgBFiThvcsXJdztErRjP4HDE2sbIMuMey1tPMsi.jpg)

Donde se especificara cual será el contexto único para todos los archivos y
donde se aplicara.

![](https://ecoding.tech/storage/images/EolAqyl75JWD1U42pjz2A48xpTy6YEGG3vKN6s6t.jpg)

Y listo, ahora nuestras importación se basaran desde la carpeta “src” que
especificamos como carpeta raíz.

![](https://ecoding.tech/storage/images/g68YXMJCqxGad7EgzJWsrGWznfVGIF2yOi8b2eQS.jpg)


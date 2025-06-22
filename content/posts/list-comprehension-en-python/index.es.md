---
title: "List Comprehension en Python"
date: "2022-03-17 10:36:46"
lastmod: "2022-03-17 10:36:46"
draft: false
authors: ['Melio']
description: "Breve introducción a la sintaxis corta que ofrece python para la creación de una lista basada en los valores de otra. List Comprehension&nbsp;"
featuredImage: ""
tags: ['PHP', 'Laravel', 'Controller', 'Backend', 'Auth']
categories: ['Laravel']
---
# List Comprehension en Python

_ <p>Breve introducción a la sintaxis corta que ofrece python para la creación
de una lista basada en los valores de otra. List Comprehension&nbsp;</p> _

__hace 3 años -___321 visitas_

**List Comprehension**

A partir de la versión 2.0 de python, se agrego esta short sintaxis para la
creación de listas basadas en otra. Esta no es la única forma de realizar esta
tarea, también se tiene opciones como la estructura for, las funciones de
orden superior como map, filter y otros, pero esta opción proporciona una
sintaxis corta y fácil de entender.

**Sintaxis**

    
    
    [expression for member in iterable]

**Ejemplos**

    
    
    list_letters = [letter for letter in "Cadena"]
    print(list_letters)

Como resultado:

    
    
    ['C', 'a', 'd', 'e', 'n', 'a']

  * **Aplicando condicionales para el filtrado**

Filtrando nombres que contengan la letra ‘x’

    
    
    names = ["Abel", "Andree", "Roxana", "Xavier", "Juelix", "Fabrizio"]
    names_with_x = [name for name in names if "X" in name.upper()]
    print(names_with_x)

Como resultado:

    
    
    ['Roxana', 'Xavier', 'Juelix']

  * **Aplicando condicionales para la asignación de valores**

Determinar si cada elemento es par o impar en una lista de números enteros

    
    
    numbers = [2, 11, 17, 9, 8, 3, 12, 4, 23]
    even_or_odd = ["Par" if number%2 == 0 else "Impar" for number in numbers]
    print(even_or_odd )

Como resultado:

    
    
    ['Par', 'Impar', 'Impar', 'Impar', 'Par', 'Impar', 'Par', 'Par', 'Impar']

  * **List Comprehensions anidadas**

Determinar si cada elemento es par o impar en una lista de números enteros
desde 1 al 10

    
    
    even_or_odd = ["Par" if number%2 == 0 else "Impar" for number in [x + 1 for x in range(10)]]
    print(even_or_odd )

Como resultado:

    
    
    ['Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par', 'Impar', 'Par']

Pronto más ejemplos… \\(^o^)/


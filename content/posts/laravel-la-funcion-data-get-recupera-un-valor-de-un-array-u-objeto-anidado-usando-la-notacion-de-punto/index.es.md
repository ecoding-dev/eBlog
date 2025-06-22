---
title: "Laravel: La función data_get() recupera un valor de un array u objeto anidado usando la notación de punto"
date: "2023-02-16 02:47:20"
lastmod: "2023-02-16 02:47:20"
draft: false
authors: ['Fabrizio']
description: "La función data_get() recupera un valor de un array u objeto anidada usando la notación de punto."
featuredImage: ""
tags: ['Web Development', 'Ubuntu', 'Linux', 'Google Cloud', 'Cloud', 'Backend', 'AWS']
categories: ['Tutoriales']
---
# Laravel: La función "data_get()" recupera un valor de un array u objeto
anidado usando la notación de punto

_ <p>La función "data_get()" recupera un valor de un array u objeto anidada
usando la notación de punto.</p> _

__hace 3 años -___321 visitas_

    
    
    $data = [
        'songs' => [
            'sugar' => [
                'spotify' => 'https://open.spotify.com/track/2iuZJX9X9P0GKaE93xcPjk?si=24c26ac798b84c37',
                'video' => 'https://www.youtube.com/watch?v=09R8_2nJtjg',
            ],
            'the-scientist' => [
                'video' => 'https://www.youtube.com/watch?v=RB-RcX5DS5A',
           ],
        ]
    ];
    
    # Apuntar a cualquier clave del array u objeto
    $allTrailers = data_get($data, 'songs.*.video');
    
    # Tráiler de la película interestelar
    $trailer = data_get($data, 'songs.sugar.spotify');
    
    # Valor si no se encuentra la clave especificada.
    $imdb data_get($data, 'songs.the-scientist.spotify', 'No encontrado');


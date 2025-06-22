---
title: "Laravel redirige al destino original después de iniciar sesión o registrarse"
date: "2023-03-08 02:35:04"
lastmod: "2023-03-08 02:35:04"
draft: false
authors: ['Fabrizio']
description: "En esta publicación quiero mostrarle algunos consejos básicos para redirigir al usuario a la ruta de destino original o a alguna ruta definida con pasos simples."
featuredImage: ""
tags: []
categories: ['Laravel']
---
# Laravel redirige al destino original después de iniciar sesión o registrarse

_ <p>En esta publicación quiero mostrarle algunos consejos básicos para
redirigir al usuario a la ruta de destino original o a alguna ruta definida
con pasos simples.</p> _

__hace 3 años -___512 visitas_

Para poder enviar al usuario a la URL de destino original anterior después de
iniciar sesión es muy fácil, implementaremos el método **showLoginForm** , en
los controladores App\Http\Controllers\Auth\LoginController y
App\Http\Controllers\Auth\RegisterController.

El método se usa para poder enviar la vista del formulario, la usaremos para
previamente asignar la URL a la que nos redirigirá posterior al inicio de
sesión o registro. Nos quedaría de esta forma:

    
    
        public function showLoginForm()
        {
            if(!session()->has('url.intended'))
            {
                session(['url.intended' => url()->previous()]);
            }
            return view('auth.login');
        }

Eso seria todo, a partir de ahora va a redirigir a la pagina previa posterior
al inicio de sesión o registro, en caso de no existir una pagina previa, será
redirigida a lo asignado en la variable **$redirectTo**.


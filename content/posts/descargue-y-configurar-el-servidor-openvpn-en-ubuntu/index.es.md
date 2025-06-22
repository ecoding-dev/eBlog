---
title: "Descargue y configurar el servidor OpenVPN en Ubuntu"
date: "2022-03-19 01:11:27"
lastmod: "2022-03-19 01:11:27"
draft: false
authors: ['Fabrizio']
description: "Aprende a instalar y configurar un servidor OpenVPN en Linux para una conexión segura y privada a una red remota a través de Internet."
featuredImage: ""
tags: ['Javascript']
categories: ['Javascript']
---
#### **Instalación**

  * Descargar `openvpn-install.sh`

    
    
    💻 $ wget https://git.io/vpn -O openvpn-install.sh
    
    
    ...
    Saving to: ‘openvpn-install.sh’
    openvpn-install.sh          100%[==========================================>]  23.04K  --.-KB/s    in 0.001s  
    2023-02-14 05:41:43 (17.4 MB/s) - ‘openvpn-install.sh’ saved [23598/23598]

  * 🔒 Otorgamos permisos de ejecución

    
    
    💻 $ sudo chmod +x openvpn-install.sh

  * 🚀 Ejecutamos el script de instalación de **OpenVPN** con privilegios de superusuario

    
    
    💻 $ sudo bash openvpn-install.sh

Durante la instalación del software **OpenVPN** , se presentarán una serie de
pasos que te ayudarán a personalizar la configuración del servidor. A
continuación, se describe cada uno de los pasos y se proporciona información
útil para su configuración:

#### **Paso 1:**

¿Cuál es la dirección IPv4 pública o hostname? 🌐

En el primer paso, se te preguntará por la dirección IP pública o hostname del
servidor. Si el servidor está detrás de NAT, la dirección IP pública es
necesaria para configurar **OpenVPN**. Si no estás seguro de cuál es la
dirección IP pública o hostname, puedes preguntarle a tu proveedor de
servicios de Internet o a tu administrador de red.

    
    
    Welcome to this OpenVPN road warrior installer!
    
    This server is behind NAT. What is the public IPv4 address or hostname?
    Public IPv4 address / hostname [xx.xx.xx.xx]:

#### **Paso 2:**

¿Qué protocolo debería usar OpenVPN? 🔒

En el segundo paso, se te preguntará qué protocolo deseas utilizar para
**OpenVPN**. El protocolo **UDP** es el recomendado, ya que proporciona una
conexión más rápida y estable en comparación con **TCP**. Sin embargo, si hay
restricciones en la red que impiden el uso de **UDP** , se puede seleccionar
**TCP**.

    
    
    Which protocol should OpenVPN use?
       1) UDP (recommended)
       2) TCP
    Protocol [1]: 

#### **Paso 3:**

¿Qué puerto debe escuchar OpenVPN? 🕵️‍♂️

En el tercer paso, se te preguntará qué puerto deseas que OpenVPN escuche. El
puerto predeterminado para **OpenVPN** es el **1194** , pero si ya se está
utilizando ese puerto para otros fines, se puede seleccionar un puerto
diferente.

    
    
    What port should OpenVPN listen to?
    Port [1194]:

#### **Paso 4:**

Seleccione un servidor DNS para los clientes. 🖥️

En el cuarto paso, se te pedirá que selecciones un servidor **DNS** para los
clientes. Esto permite a los clientes resolver nombres de dominio, lo que es
importante para el acceso a Internet. Se pueden seleccionar varios servidores
**DNS** , y se recomienda elegir un servidor que esté cerca geográficamente
para minimizar la latencia.

    
    
    Select a DNS server for the clients:
       1) Current system resolvers
       2) Google
       3) 1.1.1.1
       4) OpenDNS
       5) Quad9
       6) AdGuard
    DNS server [1]:

#### **Paso 5:**

Ingrese un nombre para el primer cliente. 🧑

En el quinto paso, se te pedirá que ingreses un nombre para el primer cliente.
El cliente se utiliza para conectarse al servidor **OpenVPN** , y es
importante elegir un nombre que sea fácil de recordar y que identifique al
usuario. Si no estás seguro de qué nombre utilizar, se puede seleccionar el
nombre predeterminado **client**.

    
    
    Enter a name for the first client:
    Name [client]: 

#### **Paso 6:**

La instalación de OpenVPN está lista para comenzar. 🚀

En el sexto y último paso, se te informará que la instalación de **OpenVPN**
está lista para comenzar. Es importante leer la información proporcionada y
asegurarse de que todas las opciones sean las deseadas antes de continuar con
la instalación.

    
    
    OpenVPN installation is ready to begin.
    Press any key to continue...

Al finalizar la instalacion le va a parecer el siguiente mensaje:

    
    
    ...
    Finished!
    
    The client configuration is available in: /home/user/client.ovpn
    New clients can be added by running this script again.

  * **/home/user/client.ovpn** : Es la ruta donde se guardo el primer cliente.

#### **¿Que sigue?**

Una vez finalizada la instalación, se generarán varios archivos que son
importantes para el funcionamiento de OpenVPN:

  * **/etc/openvpn/server.conf** : este archivo es el archivo de configuración del servidor OpenVPN y se utiliza para configurar las opciones del servidor.
  * **/etc/openvpn/easy-rsa/** : esta carpeta contiene los archivos necesarios para generar certificados y claves para los clientes.
  * **/etc/openvpn/keys/** : esta carpeta contiene los certificados y claves generados para los clientes y el servidor.
  * **/etc/openvpn/openvpn-iptables.sh** : este archivo es un script que configura las reglas de iptables para permitir el tráfico de OpenVPN.
  * **/etc/systemd/system/[[email protected]](/cdn-cgi/l/email-protection)**: este archivo es el archivo de servicio de systemd que se utiliza para administrar el servicio OpenVPN.

Una vez que el servidor está instalado y configurado, el siguiente paso es
configurar los clientes. Para ello, se puede utilizar el script _**easyrsa**_
que se encuentra en la carpeta _**/etc/openvpn/easy-rsa/**_. Este script
permite **generar certificados y claves para los clientes**. Para conectarse
al servidor, los clientes deben utilizar el archivo de configuración del
cliente y los certificados generados.

#### **Crear un nuevo cliente:**

Para crear un nuevo cliente en el servidor **OpenVPN** , se puede volver a
ejecutar el script "openvpn-install.sh"

    
    
    💻 $ sudo bash openvpn-install.sh
    
    
    OpenVPN is already installed.
    
    Select an option:
       1) Add a new client
       2) Revoke an existing client
       3) Remove OpenVPN
       4) Exit

Seleccionamos la opción **Add a new client**.

Se le pedirá que ingrese un nombre para el nuevo cliente. Este nombre se
utilizará como nombre de archivo para el certificado del cliente y se
utilizará para identificar el cliente en el servidor.

    
    
    Provide a name for the client:
    Name: client2

Después de ingresar el nombre, el script generará un nuevo **certificado** y
**clave** para el cliente, y se mostrará un mensaje con datos que pueden
resultar reelevantes sobre el archivo de configuración del nuevo cliente.

    
    
    ...
    Keypair and certificate request completed. Your files are:
    req: /etc/openvpn/server/easy-rsa/pki/reqs/client2.req
    key: /etc/openvpn/server/easy-rsa/pki/private/client2.key
    Using configuration from /etc/openvpn/server/easy-rsa/pki/f6de4cca/temp.0c0be3ee
    
    
    
    
    ...
    Certificate created at:
    * /etc/openvpn/server/easy-rsa/pki/issued/client2.crt
    Inline file created:
    * /etc/openvpn/server/easy-rsa/pki/inline/client2.inline
    
    
    ...
    Prueba added. Configuration available in: /home/user/client2.ovpn

  * **/home/user/client2.ovpn** : Es la ruta donde se guardo el nuevo cliente.

#### Para comprobar si el servidor OpenVPN está corriendo, se puede utilizar
el siguiente comando:

    
    
    💻 $ sudo systemctl status openvpn-server@server

Este comando mostrará el estado actual del servicio **OpenVPN**. Si el
servicio está en ejecución, se mostrará _**active (running)**_. Si el servicio
no está en ejecución, se pueden revisar los registros en el archivo de
registro del servicio para determinar el motivo.


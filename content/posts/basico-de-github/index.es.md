---
title: "Basico de Github"
date: "2023-02-14 05:33:31"
lastmod: "2023-02-14 05:33:31"
draft: false
authors: ['Fabrizio']
description: ""GitHub: la plataforma de alojamiento de proyectos y colaboración más popular. Comparte tu código y colabora con otros desarrolladores."
featuredImage: "https://learn.microsoft.com/es-mx/training/github/introduction-to-github/media/2-issue.png"
tags: ['Ubuntu', 'OpenVPN', 'Linux', 'Cloud']
categories: ['Tutoriales']
---
## **El flujo de GitHub**

Además de ser una plataforma de desarrollo de software colaborativo, GitHub
ofrece también un flujo de trabajo diseñado para optimizar el uso de sus
diversas características. Aunque esta unidad ofrece una visión general de los
componentes importantes de la plataforma, se recomienda que primero revise
[Descripción del flujo de
GitHub](https://guides.github.com/introduction/flow/).

## **Git y GitHub**

Cuando trabaje con **Git** y **GitHub** , es posible que se pregunte en qué se
diferencian.

**Git** es un sistema de control de versiones distribuido (DVCS) que permite
que varios desarrolladores u otros colaboradores trabajen en un proyecto.
Proporciona una manera de trabajar con una o varias ramas locales e
insertarlas en un repositorio remoto. Git es responsable de todo lo que sucede
localmente en el equipo relacionado con GitHub. Entre las características
clave que ofrece Git se incluyen las siguientes:

  * Está instalado y se usa en el equipo local.
  * Se ocupa del control de versiones.
  * Admite la creación de ramas.

Para obtener más información sobre **Git** , consulte [Uso de comandos comunes
de Git](https://docs.github.com/en/free-pro-team@latest/github/using-
git/using-common-git-commands).

**GitHub** es una plataforma en la nube que usa Git como tecnología principal.
Simplifica el proceso de colaborar en proyectos y proporciona un sitio web,
herramientas de línea de comandos y un flujo global que permite a los
desarrolladores y usuarios trabajar juntos. GitHub actúa como el "repositorio
remoto" mencionado anteriormente en la sección **Git**.

Entre las características clave que ofrece GitHub se incluyen las siguientes:

  * Issues
  * Debates
  * Solicitudes de incorporación de cambios
  * Notificaciones
  * Etiquetas
  * Acciones
  * Horquillas
  * Proyectos

Para obtener más información sobre **GitHub** , consulte [Introducción a
GitHub](https://docs.github.com/en/free-pro-team@latest/github/getting-
started-with-github).

## **Incidencias**

Las **incidencias** son el elemento en el que se produce la mayor parte de la
comunicación entre los consumidores y el equipo de desarrollo de un proyecto.
Se puede crear una _incidencia_ para analizar una amplia variedad de temas,
como informes de errores, solicitudes de características, aclaraciones sobre
la documentación, etc. Una vez que se ha creado una incidencia, se puede
asignar a propietarios, etiquetas, proyectos e hitos. Las incidencias también
se pueden asociar con solicitudes de incorporación de cambios y otros
elementos de GitHub para proporcionar rastreabilidad en el futuro.

![Incidencia de GitHub que proporciona comentarios a los desarrolladores sobre
un error o una sugerencia de características.](https://learn.microsoft.com/es-
mx/training/github/introduction-to-github/media/2-issue.png)

Para obtener más información sobre las incidencias de GitHub, vea [Dominio de
las incidencias](https://guides.github.com/features/issues/).

## **Notificaciones**

Como plataforma colaborativa, GitHub ofrece **notificaciones** para
prácticamente todos los eventos que se producen en un flujo de trabajo
determinado. Estas notificaciones se pueden adaptar en función de las
preferencias. Por ejemplo, puede suscribirse a todas las creaciones y
ediciones de incidencias de un proyecto, o bien recibir notificaciones
únicamente de las incidencias en las que se le mencione. También puede decidir
si recibirá notificaciones por correo electrónico, por web y dispositivo
móvil, o ambos. Para llevar un seguimiento de todas las notificaciones en
distintos proyectos, use el [panel de notificaciones de
GitHub](https://github.com/notifications).

![Panel de notificaciones de GitHub. GitHub proporciona una bandeja de entrada
que los desarrolladores pueden usar para mantenerse al día sobre los cambios
en los repositorios.](https://learn.microsoft.com/es-
mx/training/github/introduction-to-github/media/2-notifications.png)

Para obtener más información sobre las notificaciones de GitHub, vea
[Configuración de notificaciones](https://help.github.com/github/managing-
subscriptions-and-notifications-on-github/configuring-notifications).

## **Ramas**

Las **ramas** son la manera preferida de crear cambios en el [flujo de
GitHub](https://guides.github.com/introduction/flow/). Proporcionan
aislamiento para que varias personas puedan trabajar simultáneamente en el
mismo código de manera controlada. Este modelo garantiza la estabilidad entre
las ramas críticas, como `main`, a la vez que da libertad a los
desarrolladores para confirmar los cambios que necesiten para alcanzar sus
objetivos. Una vez que el código de una rama está listo para formar parte de
la rama `main`, puede combinarse mediante una solicitud de incorporación de
cambios.

![Flujo de GitHub con una rama de características. Los cambios realizados en
una rama se pueden volver a combinar en la rama
principal.](https://learn.microsoft.com/es-mx/training/github/introduction-to-
github/media/2-branching.png)

Para obtener más información sobre las ramas de GitHub, vea [Acerca de las
ramas](https://help.github.com/github/collaborating-with-issues-and-pull-
requests/about-branches).

## **Confirmaciones**

Una **confirmación** es un cambio en uno o varios archivos de una rama. Cada
vez que se crea una confirmación, se le asigna un identificador único y se
realiza un seguimiento de ella, junto con la hora y el colaborador. Esto
proporciona un registro de auditoría claro para todas las personas que revisen
el historial de un archivo o un elemento vinculado, como una incidencia o una
solicitud de incorporación de cambios.

![Lista de las confirmaciones de GitHub en una rama
principal.](https://learn.microsoft.com/es-mx/training/github/introduction-to-
github/media/2-commits.png)

Para obtener más información sobre las confirmaciones de GitHub, vea
[Confirmación y revisión de cambios en el
proyecto](https://help.github.com/desktop/contributing-to-projects/committing-
and-reviewing-changes-to-your-project).

## **Solicitudes de incorporación de cambios**

Una **solicitud de incorporación de cambios** es un mecanismo que sirve para
indicar que las confirmaciones de una rama están listas para combinarse en
otra. El desarrollador que envíe la **solicitud de incorporación de cambios**
normalmente solicitará a uno o varios revisores que comprueben el código y
aprueben la combinación. Estos revisores podrán comentar los cambios, agregar
otros o usar la solicitud de incorporación de cambios para realizar un
análisis más exhaustivo. Una vez que los cambios se hayan aprobado (en caso de
que se requiera aprobación), la rama de origen de la solicitud de
incorporación de cambios (la rama de comparación) se podrá combinar con la
rama base.

![Las solicitudes de incorporación de cambios de GitHub proporcionan una
manera de obtener confirmaciones de una rama en
otra.](https://learn.microsoft.com/es-mx/training/github/introduction-to-
github/media/2-pull-request.png)

Para obtener más información sobre las solicitudes de incorporación de cambios
de GitHub, vea [Acerca de las solicitudes de incorporación de
cambios](https://help.github.com/github/collaborating-with-issues-and-pull-
requests/about-pull-requests).

## **Etiquetas**

Las etiquetas proporcionan una manera de categorizar y organizar las
**incidencias** y las **solicitudes de incorporación de cambios** en un
repositorio. A medida que cree un repositorio de GitHub, se agregarán
automáticamente varias etiquetas y también se pueden crear otras nuevas.

Estos son algunos ejemplos de etiquetas:

  * error
  * en línea
  * duplicar
  * help-wanted
  * mejora
  * question

![Las etiquetas de GitHub se pueden usar para clasificar las incidencias y las
solicitudes de incorporación de cambios relacionadas con el repositorio de
GitHub.](https://learn.microsoft.com/es-mx/training/github/introduction-to-
github/media/2-labels.png)

Para obtener más información sobre las etiquetas de GitHub, vea [Acerca de las
etiquetas](https://docs.github.com/en/free-pro-team@latest/github/managing-
your-work-on-github/about-labels).

## **Acciones**

Las **acciones de GitHub** proporcionan funcionalidad de flujo de trabajo y
automatización de tareas en un repositorio. Las acciones se pueden usar para
simplificar los procesos del ciclo de vida de desarrollo de software e
implementar la integración y la implementación continuas (CI/CD).

Acciones de GitHub se compone de lo siguiente:

  * **Flujos de trabajo** : procesos automatizados que se han agregado al repositorio.
  * **Eventos** : actividades que desencadenan un flujo de trabajo.
  * **Trabajos** : conjunto de pasos que se ejecutan en un ejecutor.
  * **Pasos** : tarea que puede ejecutar uno o varios comandos (acciones).
  * **Acciones** : comandos independientes que se pueden combinar en pasos. Se pueden combinar varios pasos para crear un trabajo.
  * **Ejecutores** : servidor que tiene instalada la aplicación de ejecutor de Acciones de GitHub.

![Las acciones de GitHub proporcionan una forma de automatizar el ciclo de
vida de desarrollo de software.](https://learn.microsoft.com/es-
mx/training/github/introduction-to-github/media/2-actions.png)

Para obtener más información sobre las acciones de GitHub, consulte
[Introducción a Acciones de GitHub](https://docs.github.com/en/free-pro-
team@latest/actions/learn-github-actions/introduction-to-github-actions).

## **Clonación y bifurcación**

GitHub proporciona varias maneras de copiar un repositorio para poder trabajar
en él.

  * **Clonar un repositorio** : al clonar un repositorio, se realizará una copia del repositorio y de su historial en el equipo local. Si tiene acceso de escritura al repositorio, puede enviar los cambios de la máquina local al repositorio remoto (denominado **origen**) a medida que se completan. Para clonar un repositorio, puede usar el comando [`git clone [url]`](https://docs.github.com/en/free-pro-team@latest/github/using-git/getting-changes-from-a-remote-repository#cloning-a-repository) o el comando [`gh repo clone [url]`](https://cli.github.com/manual/gh_repo_clone) de la CLI de GitHub.
  * **Bifurcación de un repositorio** : al bifurcar un repositorio, se realiza una copia del repositorio en la cuenta de GitHub. El repositorio principal se denomina **ascendente** , mientras que la copia bifurcada se conoce como **origen**. Una vez que haya bifurcado un repositorio en la cuenta de GitHub, puede **clonarlo** en el equipo local. La bifurcación permite realizar cambios libremente en un proyecto sin afectar al repositorio **ascendente** original. Para contribuir con cambios en el repositorio ascendente, cree una **solicitud de incorporación de cambios** desde el repositorio bifurcado. También puede ejecutar comandos `git` para asegurarse de que la copia local permanezca sincronizada con el repositorio **ascendente**.

¿Cuándo debería clonar un repositorio en lugar de bifurcarlo? Si está
trabajando con un repositorio y tiene acceso de escritura, puede clonarlo en
el equipo local. Desde allí, puede realizar modificaciones e introducir los
cambios directamente en el repositorio de **origen**.

Si necesita trabajar con un repositorio creado por otro propietario, como
`github/example`, y no tiene acceso de escritura, puede bifurcar el
repositorio en su cuenta de GitHub y, luego, clonar la bifurcación en el
equipo local. Para representarlo visualmente, supongamos que su cuenta de
GitHub se denomina `githubtraining`. A través del sitio web de GitHub, puede
bifurcar `github/example` o cualquier otro repositorio en su cuenta. Desde
allí, puede clonar la versión bifurcada del repositorio en el equipo local.
Estos pasos se muestran en la imagen siguiente.

![La bifurcación de un repositorio crea una copia de este en su cuenta de
GitHub. Después, puede clonar la copia bifurcada del repositorio en el equipo
local.](https://learn.microsoft.com/es-mx/training/github/introduction-to-
github/media/2-fork-clone.png)

Se pueden realizar cambios en la copia local de `githubtraining/example` y,
luego, volver a insertarlos en el repositorio de **origen** remoto
(`githubtraining/example`). Posteriormente, los cambios se pueden enviar al
repositorio `github/example`**ascendente** mediante una **solicitud de
incorporación de cambios** , como se muestra a continuación.

![Los cambios locales pueden insertarse en el repositorio de origen y, luego,
se puede crear una solicitud de incorporación de cambios para obtener los
cambios en el repositorio ascendente.](https://learn.microsoft.com/es-
mx/training/github/introduction-to-github/media/2-fork-pullrequest.png)

Para obtener más información, consulte [bifurcar un
repositorio](https://docs.github.com/en/free-pro-team@latest/github/getting-
started-with-github/fork-a-repo).

## **GitHub Pages**

**GitHub Pages** es un motor de hospedaje que está integrado directamente en
la cuenta de GitHub. Si sigue una serie de convenciones y habilita la
característica, puede crear su propio sitio estático generado a partir de
código HTML y Markdown extraído directamente del repositorio.

![GitHub Pages es un motor de hospedaje que está disponible en la cuenta de
GitHub. Se puede usar para hospedar sitios estáticos generados desde el
repositorio.](https://learn.microsoft.com/es-mx/training/github/introduction-
to-github/media/2-github-pages.png)

Para obtener más información, vea [GitHub Pages](https://pages.github.com/).


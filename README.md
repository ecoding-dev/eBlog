# Blog de Ecoding

Este repositorio contiene el código fuente del blog del equipo **Ecoding**. El sitio está construido con [Hugo](https://gohugo.io/), utilizando el tema [DoIt](https://github.com/HEIGE-PCloud/DoIt) y soporta contenido en inglés y español.

## Autores
- **Fabrizio Piminchumo** – Seguridad Digital
- **Abel Llontop** – Front Developer
- **Melio Diaz** – Backend
- **Arnaldo Farro** – Backend

## Estructura del proyecto
- `content/` – Entradas y páginas del sitio.
- `data/authors/` – Archivos TOML con la información de cada autor.
- `config/` – Archivos de configuración de Hugo.
- `themes/DoIt` – Tema utilizado por el sitio.
- `public/` – Versión generada del sitio (HTML estático).

## Uso
Para iniciar un servidor de desarrollo:

```bash
hugo server -D
```

Para generar el sitio estático:

```bash
hugo --minify
```

Es necesario tener instalado Go y Hugo Extended. El módulo Go se describe en `go.mod` y permite obtener el tema automáticamente.

## Funciones y capacidades
- Soporte multilenguaje.
- Shortcodes para incrustar contenido multimedia y diagramas.
- Sistema de taxonomías (categorías, etiquetas y series).
- Soporte opcional para PWA.

## Licencia
El contenido se distribuye bajo la licencia presente en `LICENSE`.

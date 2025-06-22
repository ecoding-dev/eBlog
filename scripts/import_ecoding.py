import os
import re
import requests
from readability import Document
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urlparse

AUTHOR_MAP = {
    'Fabrizio Piminchumo': 'Fabrizio',
    'Abel Llontop': 'Abel',
    'Melio Diaz': 'Melio',
    'Arnaldo Farro': 'Arnaldo',
    'labelito': 'Abel',
    'Andree Farro': 'Arnaldo',
    'Melio Diaz Diaz': 'Melio',
}

URLS = [
    'https://ecoding.dev/p/basico-de-github-575',
    'https://ecoding.dev/p/comandos-de-git-282',
    'https://ecoding.dev/p/descargar-nginx-y-configurar-el-reverse-proxy-en-ubuntu-967',
    'https://ecoding.dev/p/descargue-y-configurar-el-servidor-openvpn-en-ubuntu',
    'https://ecoding.dev/p/laravel-la-funcion-data-get-recupera-un-valor-de-un-array-u-objeto-anidado-usando-la-notacion-de-punto',
    'https://ecoding.dev/p/especificar-directorio-raiz-para-el-uso-mas-comodo-de-importaciones-de-modulos-javascript-en-visual-code',
    'https://ecoding.dev/p/list-comprehension-en-python',
    'https://ecoding.dev/p/como-poner-sombras-a-un-poligono-con-css',
    'https://ecoding.dev/p/laravel-redirige-al-destino-original-despues-de-iniciar-sesion-o-registrarse',
]

OUTPUT_DIR = os.path.join('content', 'posts')
# Images will not be downloaded during the import process. They will remain
# referenced by their original URLs. A separate node script can later download
# them if desired.

def slug_from_url(url: str) -> str:
    slug = urlparse(url).path.strip('/')
    slug = slug.split('/')[-1]
    slug = re.sub(r'-\d+$', '', slug)
    return slug


def fetch_html(url: str) -> str:
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def extract_metadata(soup: BeautifulSoup) -> dict:
    meta = {}
    title = soup.find('title')
    if title:
        meta['title'] = title.text.strip()
    desc = soup.find('meta', {'name': 'description'})
    if desc:
        meta['description'] = desc.get('content', '').strip()
    author_tag = soup.find('p', class_='author-name')
    if author_tag:
        meta['author'] = author_tag.get_text(strip=True)
    else:
        author = soup.find('meta', {'name': 'author'})
        if author:
            meta['author'] = author.get('content', '').strip()
    date = soup.find('meta', {'itemprop': 'datePublished'})
    if date:
        meta['date'] = date.get('content', '').strip()
    section = soup.find('meta', {'itemprop': 'articleSection'})
    if section:
        meta['category'] = section.get('content', '').strip()
    keywords = soup.find('meta', {'name': 'keywords'})
    if keywords:
        meta['tags'] = [k.strip() for k in keywords.get('content', '').split(',') if k.strip()]
    return meta


def download_image(url: str, slug: str, idx: int) -> str:
    """Return the original image URL without downloading.

    Downloading is deferred to a separate script so that the repository does
    not contain binary image files. This function simply returns the provided
    URL so that it can be written directly into the markdown content.
    """
    return url


def convert_article(html: str, slug: str):
    article_html = Document(html).summary(html_partial=True)
    soup = BeautifulSoup(article_html, 'lxml')
    images = soup.find_all('img')
    for idx, img in enumerate(images, start=1):
        src = img.get('src')
        if not src:
            continue
        new_src = download_image(src, slug, idx)
        img['src'] = new_src
    markdown = html2text.HTML2Text()
    markdown.ignore_links = False
    md = markdown.handle(str(soup))
    return md, images[0]['src'] if images else None


def write_post(slug: str, meta: dict, body_md: str, featured: str):
    post_dir = os.path.join(OUTPUT_DIR, slug)
    os.makedirs(post_dir, exist_ok=True)
    front_matter = {
        'title': meta.get('title', slug),
        'date': meta.get('date', ''),
        'lastmod': meta.get('date', ''),
        'draft': False,
        'authors': [AUTHOR_MAP.get(meta.get('author', ''), meta.get('author', ''))],
        'description': meta.get('description', ''),
        # Keep the original image URL so that a follow-up script can download it
        # later. The Node.js helper will replace these URLs with local paths
        # once the images are saved.
        'featuredImage': featured or '',
        'tags': meta.get('tags', []),
        'categories': [meta.get('category', '')] if meta.get('category') else [],
    }
    fm_lines = ['---']
    for k, v in front_matter.items():
        if isinstance(v, list):
            fm_lines.append(f"{k}: {v}")
        elif isinstance(v, bool):
            fm_lines.append(f"{k}: {str(v).lower()}")
        else:
            fm_lines.append(f"{k}: \"{v}\"")
    fm_lines.append('---\n')
    content = '\n'.join(fm_lines) + body_md
    with open(os.path.join(post_dir, 'index.es.md'), 'w') as f:
        f.write(content)


def main():
    for url in URLS:
        print('Processing', url)
        slug = slug_from_url(url)
        html = fetch_html(url)
        soup = BeautifulSoup(html, 'lxml')
        meta = extract_metadata(soup)
        body_md, featured = convert_article(html, slug)
        write_post(slug, meta, body_md, featured)

if __name__ == '__main__':
    main()

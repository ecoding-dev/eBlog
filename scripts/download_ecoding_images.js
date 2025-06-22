#!/usr/bin/env node
// Utility script to download remote images hosted on ecoding.dev for each post.
// It replaces the remote URLs in the markdown files with the downloaded file
// name. This script is meant to be run manually and is not part of the normal
// build process.

const fs = require('fs');
const path = require('path');
const https = require('https');

function download(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    https.get(url, res => {
      if (res.statusCode !== 200) {
        file.close();
        fs.unlinkSync(dest);
        return reject(new Error(`Request failed ${res.statusCode}`));
      }
      res.pipe(file);
      file.on('finish', () => file.close(resolve));
    }).on('error', err => {
      fs.unlink(dest, () => reject(err));
    });
  });
}

async function processFile(file) {
  let content = fs.readFileSync(file, 'utf8');
  const slug = path.basename(path.dirname(file));
  const regex = /!\[[^\]]*\]\((https:\/\/ecoding\.dev[^)]+)\)/g;
  let match;
  let index = 1;
  while ((match = regex.exec(content)) !== null) {
    const url = match[1];
    const ext = path.extname(url.split('?')[0]) || '.png';
    const filename = `${slug}-${index}${ext}`;
    const dest = path.join(path.dirname(file), filename);
    try {
      await download(url, dest);
      content = content.replace(url, filename);
      index++;
    } catch (err) {
      console.error(`Failed to download ${url}:`, err.message);
    }
  }
  fs.writeFileSync(file, content);
}

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    if (entry.isFile() && entry.name === 'index.es.md') processFile(full);
  }
}

walk(path.join(__dirname, '..', 'content', 'posts'));


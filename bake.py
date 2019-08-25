#!/usr/bin/env python3
# bake the configuration envvars into `boot.js`
# the logic is copied from `generateBootScript` in `gulp.js`

import os
from pathlib import Path

root_path = Path(__file__).parent
build_path = root_path / 'build'
env = os.environ
liquid_domain = os.environ['LIQUID_DOMAIN']
asset_root = f"https://client.hypothesis.{liquid_domain}/"
sidebar_app_url = f"https://hypothesis.{liquid_domain}/app.html"


def generate_boot_js():
    with (build_path / 'manifest.json').open(encoding='utf8') as f:
        manifest = f.read().strip()

    with (build_path / 'scripts/boot.bundle.js').open(encoding='utf8') as f:
        src = f.read()

    src = src.replace('__MANIFEST__', manifest)
    src = src.replace('__ASSET_ROOT__', asset_root)
    src = src.replace('__SIDEBAR_APP_URL__', sidebar_app_url)

    with (build_path / 'boot.js').open('wt', encoding='utf8') as f:
        f.write(src)


def generate_nginx_conf():
    with (root_path / 'nginx.conf').open(encoding='utf8') as f:
        nginx_conf = f.read()

    nginx_conf = nginx_conf.replace('${liquid_domain}', liquid_domain)
    nginx_conf = nginx_conf.replace('${root_path}', str(root_path))

    with open('/etc/nginx/conf.d/h-client.conf', 'w', encoding='utf8') as f:
        f.write(nginx_conf)


if __name__ == '__main__':
    generate_boot_js()
    generate_nginx_conf()

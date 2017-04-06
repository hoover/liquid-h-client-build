#!/usr/bin/env python3
# bake the configuration envvars into `boot.js`
# the logic is copied from `generateBootScript` in `gulp.js`

import os
from pathlib import Path

def generate_boot_js(build):
    with (build / 'manifest.json').open(encoding='utf8') as f:
        manifest = f.read().strip()

    with (build / 'scripts' / 'boot.bundle.js').open(encoding='utf8') as f:
        src = f.read()

    src = src.replace('__MANIFEST__', manifest)
    src = src.replace('__ASSET_ROOT__', os.environ['ASSET_ROOT'])
    src = src.replace('__SIDEBAR_APP_URL__', os.environ['SIDEBAR_APP_URL'])
    src = src.split('//# sourceMappingURL=')[0]

    with (build / 'boot.js').open('wt', encoding='utf8') as f:
        f.write(src)

if __name__ == '__main__':
    generate_boot_js(Path(__file__).parent / 'build')

#!/usr/bin/env python3

import os

PKG_DIR = '/var/cache/manjaro-tools/pkg/stable/x86_64'

packages = {
    'hydrogen-theme': 'https://aur.archlinux.org/hydrogen-theme.git',
}

if __name__ == '__main__':
    # Clone git repos.
    for pkg in packages.keys():
        print('[' + pkg + ']')
        git = packages[pkg]
        os.system('cd pkgbuild ; git clone ' + git)

    # Using buildpkg command.
    for pkg in packages.keys():
        os.system('cd pkgbuild ; buildpkg -p ' + pkg)

    # Copy packages.
    os.system('rm -rf ./laniakea-repo')
    os.system(f'cp -r {PKG_DIR} ./laniakea-repo')

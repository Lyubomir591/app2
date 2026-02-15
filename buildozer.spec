[app]
title = OrderManager
package.name = ordermanager
package.domain = org.ordermanager

version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.exclude_dirs = tests, bin, .git, .github, .buildozer
source.exclude_patterns = .gitignore, README.md

source.main.py = main.py

requirements = 
    python3==3.11,
    kivy==2.3.0,
    pillow==10.2.0,
    requests==2.31.0,
    android==1.0.0

# Обязательные ресурсы
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/splash.png

orientation = portrait
fullscreen = 0

# Android требования 2026
android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 34
android.minapi = 24
android.ndk = 26b
android.ndk_api = 24
android.archs = arm64-v8a

android.accept_sdk_license = True
android.enable_androidx = True
android.extra_manifest_xml = <application android:requestLegacyExternalStorage="true" />

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin
build_cache = 1

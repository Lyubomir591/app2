[app]
title = OrderManager
package.name = ordermanager
package.domain = org.ordermanager

version = 1.0.20260216

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
source.exclude_dirs = tests, bin, .git, .github, .buildozer, __pycache__
source.exclude_patterns = .gitignore, README.md, LICENSE

source.main.py = main.py

# === СОВРЕМЕННЫЕ ЗАВИСИМОСТИ 2026 ===
requirements = 
    python3==3.11,
    kivy==2.3.0,
    pillow==10.2.0,
    requests==2.31.0,
    android==1.0.0,
    setuptools,
    packaging

# === ИКОНКИ И СПЛЭШ (обязательно для сборки) ===
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/splash.png
icon.density = xxxhdpi

orientation = portrait
fullscreen = 0

# === СОВРЕМЕННЫЕ ТРЕБОВАНИЯ ANDROID 2026 ===
android.permissions = 
    INTERNET,
    ACCESS_NETWORK_STATE,
    READ_EXTERNAL_STORAGE,
    WRITE_EXTERNAL_STORAGE

android.api = 34
android.minapi = 24
android.ndk = 26b
android.ndk_api = 24

# === ТОЛЬКО 64-БИТНЫЕ АРХИТЕКТУРЫ (требование Google Play 2026) ===
android.archs = arm64-v8a

android.accept_sdk_license = True

# === ВАЖНО: Экспорт активити для Android 12+ ===
android.extra_manifest_xml = <application android:requestLegacyExternalStorage="true" />

# === Оптимизации ===
android.enable_androidx = True
android.enable_backup = False
android.ouya.category = None

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin

# === КЭШИРОВАНИЕ ДЛЯ УСКОРЕНИЯ СБОРКИ ===
build_cache = 1

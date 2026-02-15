[app]
title = OrderManager
package.name = ordermanager
package.domain = org.ordermanager
version = 1.0.0
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.main.py = main.py

# СТАБИЛЬНЫЕ ВЕРСИИ (без ошибок!)
requirements = python3==3.10.12,kivy==2.2.1,cython==0.29.33,android,pillow,requests
fullscreen = 0
orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# КРИТИЧЕСКИ ВАЖНО: стабильные версии и автоматическое принятие лицензий!
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools = 33.0.0
android.accept_sdk_license = True
android.archs = arm64-v8a,armeabi-v7a
p4a.bootstrap = sdl2
android.debug = True

[buildozer]
build_dir = ./.buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 1
source.exclude_dirs = tests, bin, .git, .github, .buildozer, __pycache__
source.exclude_patterns = .gitignore, .github/, README.md, *.pyc, *.pyo
colored_log = 1
buildozer.ignore_env = 1
p4a.branch = stable

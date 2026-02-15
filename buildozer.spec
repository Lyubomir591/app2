[app]

# Название приложения
title = OrderManager

# ID пакета
package.name = ordermanager
package.domain = org.ordermanager

# Версия
version = 1.0.0

# Исходный файл
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

# Главный файл
source.main.py = main.py

# Требования (стабильные версии)
requirements = python3==3.10.12,kivy==2.2.1,cython==0.29.33,android,pillow,requests

# Полноэкранный режим
fullscreen = 0

# Ориентация
orientation = portrait

# Разрешения (для Android 10+)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE

# API Level (СТАБИЛЬНЫЕ ВЕРСИИ!)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools = 33.0.0

# КРИТИЧЕСКИ ВАЖНО: автоматическое принятие лицензий
android.accept_sdk_license = True

# Архитектуры
android.archs = arm64-v8a,armeabi-v7a

# Bootstrap (современный синтаксис)
p4a.bootstrap = sdl2

# Режим отладки
android.debug = True

# Метаданные
android.meta_data = 

# Лицензия
license.name = MIT
license.file = LICENSE

[buildozer]

# Директории сборки
build_dir = ./.buildozer
bin_dir = ./bin

# Логирование
log_level = 2

# Предупреждение при запуске от root
warn_on_root = 1

# Исключения из сборки
source.exclude_dirs = tests, bin, .git, .github, .buildozer, __pycache__
source.exclude_patterns = .gitignore, .github/, README.md, *.pyc, *.pyo

# Цветные логи
colored_log = 1

# Очистка перед сборкой
buildozer.ignore_env = 1

# Использовать стабильную ветку p4a
p4a.branch = stable

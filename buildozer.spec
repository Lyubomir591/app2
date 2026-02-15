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

# Требования (стабильные версии для совместимости)
requirements = python3==3.10.12,kivy==2.2.1,cython==0.29.33,android,pillow,requests

# Иконка и сплэш (закомментированы если файлы отсутствуют)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splash.png

# Полноэкранный режим
fullscreen = 0

# Ориентация
orientation = portrait

# Разрешения
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE

# API Level (стабильные версии)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools = 33.0.0

# Автоматическое принятие лицензий (КРИТИЧЕСКИ ВАЖНО для CI/CD)
android.accept_sdk_license = True

# Архитектуры
android.archs = arm64-v8a,armeabi-v7a

# Bootstrap (обязательно для Kivy)
android.bootstrap = sdl2

# Режим отладки
android.debug = True

# Метаданные
android.meta_data = 

# Сервисы (если нужны)
services = 

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

# Очистка перед сборкой (для CI/CD)
buildozer.ignore_env = 1

# Использовать локальный репозиторий p4a (для стабильности)
p4a.branch = stable

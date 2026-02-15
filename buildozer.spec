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

# Требования
requirements = python3,kivy==2.2.1,requests,android,pillow

# Иконка и сплэш
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/splash.png

# Полноэкранный режим
fullscreen = 0

# Ориентация
orientation = portrait

# Разрешения
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE

# API Level
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Архитектуры
android.archs = arm64-v8a,armeabi-v7a

# Режим отладки
android.debug = True

# Файл настроек
android.meta_data = 

# Сервисы (если нужны)
services = 

# Лицензия
license.name = MIT
license.file = LICENSE

[buildozer]

# Команды для выполнения перед сборкой
build_dir = ./.buildozer
bin_dir = ./bin

# Логирование
log_level = 2

# Clean build
warn_on_root = 1

# Игнорировать файлы
source.exclude_dirs = tests, bin, .git, .github, .buildozer
source.exclude_patterns = .gitignore, .github/, README.md

# Использовать цвета в логах
colored_log = 1
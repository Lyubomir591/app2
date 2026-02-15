#!/usr/bin/env python3
"""
Скрипт для автоматического обновления buildozer.spec
"""
import re
import os
from datetime import datetime

def update_buildozer_spec():
    """Обновление файла конфигурации"""
    
    spec_file = 'buildozer.spec'
    
    if not os.path.exists(spec_file):
        print("❌ Файл buildozer.spec не найден!")
        return False
    
    with open(spec_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Обновление версии
    current_date = datetime.now().strftime('%Y%m%d')
    new_version = f'1.0.{current_date}'
    
    content = re.sub(
        r'version\s*=\s*.*',
        f'version = {new_version}',
        content
    )
    
    # Обновление требований
    requirements = 'python3,kivy==2.2.1,requests,android,pillow'
    content = re.sub(
        r'requirements\s*=\s*.*',
        f'requirements = {requirements}',
        content
    )
    
    # Установка архитектур
    archs = 'arm64-v8a, armeabi-v7a'
    content = re.sub(
        r'android\.archs\s*=\s*.*',
        f'android.archs = {archs}',
        content
    )
    
    with open(spec_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ buildozer.spec обновлен")
    print(f"   Версия: {new_version}")
    print(f"   Архитектуры: {archs}")
    
    return True

if __name__ == '__main__':
    update_buildozer_spec()
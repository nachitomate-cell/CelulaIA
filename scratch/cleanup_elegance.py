import os
import shutil
import json

base_path = r'c:\Users\56983\OneDrive\Desktop\CelulaIA'

# 1. Folders to delete
folders_to_delete = [
    'js',
    'backend',
    'instancia-2',
    'pages',
    'css',
    '.claude',
    '.vercel'
]

for folder in folders_to_delete:
    path = os.path.join(base_path, folder)
    if os.path.exists(path):
        print(f"Deleting folder: {folder}")
        shutil.rmtree(path)

# 2. Files to delete
files_to_delete = [
    'server.err.log',
    'server.out.log'
]

for file in files_to_delete:
    path = os.path.join(base_path, file)
    if os.path.exists(path):
        print(f"Deleting file: {file}")
        os.remove(path)

# 3. Clean settings.local.json
settings_path = os.path.join(base_path, 'settings.local.json')
if os.path.exists(settings_path):
    with open(settings_path, 'r', encoding='utf-8') as f:
        settings = json.load(f)
    
    # Remove any strings containing "Ferraza" or "Barberos"
    if 'permissions' in settings and 'allow' in settings['permissions']:
        settings['permissions']['allow'] = [
            p for p in settings['permissions']['allow'] 
            if 'Ferraza' not in p and 'Barberos' not in p
        ]
    
    with open(settings_path, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=2)
    print("Cleaned settings.local.json")

print("\n=== CLEANUP FINISHED: 100% ELEGANCE ===")

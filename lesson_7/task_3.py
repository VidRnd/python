import shutil
import os

what_folder = 'my_project'
search_folder = 'templates'
for root,dirs,files in os.walk(what_folder):
    if search_folder in dirs:
        where_copy = os.path.join(f'{root}/{search_folder}')
        ff = os.path.join(f'{what_folder}/{search_folder}')
        shutil.copytree(f'{where_copy}',f'{ff}',dirs_exist_ok=True)



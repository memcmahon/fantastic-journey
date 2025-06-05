import sys
import os
import shutil

from copystatic import copy_files_recursive
from contentgenerator import generate_pages

if len(sys.argv) > 0:
    basepath = sys.argv[0]
else:
    basepath = "/"


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages(basepath, dir_path_content, template_path, dir_path_public)


main()

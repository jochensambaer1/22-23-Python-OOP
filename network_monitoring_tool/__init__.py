import os

directory_path = "/path/to/package"
file_path = os.path.join(directory_path, "__init__.py")

open(file_path, 'a').close()

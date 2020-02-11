import os


def get_file_content(filepath):
    with open(filepath, "r") as f:
        return f.read()

def get_path(path):
    path = os.path.normpath(path)
    if os.path.isabs(path):
        print(path)
    else:
        path = os.path.join(os.getcwd(), path)
        print(path)

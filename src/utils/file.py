import os

def absolute_file_path(filepath):
    basePath = os.path.split(os.path.dirname(__file__))[0]
    rootPath = os.path.split(basePath)[0]
    realPath = os.path.join(rootPath, filepath)
    return realPath
import os

def load_credential_from_file(filepath):
    basePath = os.path.split(os.path.dirname(__file__))[0]
    rootPath = os.path.split(basePath)[0]
    realPath = os.path.join(rootPath, filepath)

    with open(realPath, "rb") as f:
        return f.read()

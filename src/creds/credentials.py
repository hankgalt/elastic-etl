import os
from utils.file import absolute_file_path

def load_file(filepath):
    real_path = absolute_file_path(filepath)
    return real_path

def load_credential_from_file(filepath):
    real_path = absolute_file_path(filepath)
    with open(real_path, "rb") as f:
        return f.read()

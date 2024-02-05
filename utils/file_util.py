import os
import pkg_resources
import uuid


def get_root_path():
    package_path = pkg_resources.resource_filename(__name__, "")
    parent_path = os.path.dirname(package_path)
    return parent_path


def get_file_paths(directory):
    file_paths = []

    # iterate all files in the directory
    for root, directories, files in os.walk(directory):
        for file in files:
            # construct full path
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    return file_paths


def get_folder_file_list(folder_path):
    file_paths = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_paths.append(file_path)
    return file_paths


def create_unique_folder(parent_path):
    unique_id = str(uuid.uuid4())
    folder_path = os.path.join(parent_path, unique_id)
    os.mkdir(folder_path)
    return folder_path


from importlib.metadata import version
import os
import yaml

def get_version():
    try:
        version_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'poja-version.yml')
        with open(version_file_path) as version_file:
            parsed_version_file = yaml.load(version_file, Loader=yaml.FullLoader)
            return parsed_version_file["version"]
        # with open("poja-version.yml") as version_file:
        #     parsed_version_file = yaml.load(version_file, Loader=yaml.FullLoader)
        #     return parsed_version_file["version"]
    except FileNotFoundError:
        # if no local version file is found
        # then we suppose the call comes from installed package
        # and we just return the installed version
        return version("poja")

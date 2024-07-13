from setuptools import setup, find_packages
from poja.version import get_version


def get_long_description():
    with open("README.md", "r") as readme:
        return readme.read()


with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="dname-code-gen",
    version=get_version(),
    description="Serverless Postgres+Java hosted on Github+AWS",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Daris02",
    author_email="hei.raymond.2@gmail.com",
    url="https://github.com/Daris02/code-gen-cli",
    packages=find_packages(exclude=["tests*"]),
    install_requires=required,
)

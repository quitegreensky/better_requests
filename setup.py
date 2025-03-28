
from setuptools import setup, find_packages
import better_requests
requirements_path='requirements.txt'

with open("README.md", "r") as fh:
    long_description = fh.read()

def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements(requirements_path)
setup(
    name=better_requests.__package_name__,
    version=str(better_requests.__version__),
    description=better_requests.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=better_requests.__url__,
    author=better_requests.__author__,
    author_email=better_requests.__email__,
    license='MIT',
    install_requires=parse_requirements(requirements_path) ,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
      )
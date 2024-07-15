from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup( name="img-preprocess-pipeline",
    version="0.0.1",
    author="Pablo Francisco",
    author_email="pablo.fco.melo@gmail.com",
    description="Customized library for preprocessing images",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pablo-francisco/img-preprocess-pipeline",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)
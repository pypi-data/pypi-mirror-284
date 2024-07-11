from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='maquina_escribir',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    author='Miguel Durán',
    description='Una maquina de escribir simple',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
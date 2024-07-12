from setuptools import setup, find_packages

with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()
    
setup(
    name="albertdomprojecte1",
    version="0.5.0",
    packages=find_packages(),
    install_requires=[],
    author="Albert Domènech",
    description="Biblioteca per a consultar cursos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hack4u.io",
)   

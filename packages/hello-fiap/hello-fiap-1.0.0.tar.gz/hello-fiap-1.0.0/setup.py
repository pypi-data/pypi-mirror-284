from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='hello-fiap',
    version='1.0.0',
    packages=find_packages(),
    description='Uma biblioteca para demonstrar como subir no pypi',
    author='Thiago S Adriano',
    author_email='tadriano.dev@teste.com',
    url='https://github.com/tadrianonet/hello',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown' 
)
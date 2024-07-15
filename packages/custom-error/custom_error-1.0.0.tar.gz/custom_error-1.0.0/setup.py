'''Setup'''
from setuptools import setup, find_packages

def read_file(filename:str) -> str:
    '''Read file text - README and LICENSE'''
    with open(f'./{filename}', 'r', encoding='utf-8') as f:
        file = f.read()
    return file

setup(
    name='custom_error',
    version='1.0.0',
    package_dir={'':'src'},
    packages=find_packages('src'),
    install_requires=['colorama'],
    description='Create your custom errors and I have control of them with Custom Error',
    license=read_file('LICENSE'),
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Anthony Carrillo',
    author_email='anthonyzok521@gmail.com',
    url='https://github.com/Anthonyzok521/pypi-custom-error',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    keywords=[
        'custom error',
        'custom_error', 
        'python error', 
        'error', 
        'custom exception', 
        'custom', 
        'python exception', 
        'exception', 
        'custom_exception'
    ]
)

# setup.py

from setuptools import setup, find_packages

setup(
    name='django-include-apps',    
    version='0.1.0',               
    packages=find_packages(),
    install_requires=[
        'typer',                   
        'requests',
        'inquirer'
    ],
    entry_points={
        'console_scripts': [
            'django-include-apps=django_include_apps.main:app',   
        ],
    },
    author='ROHAN',
    author_email='rohanroni2019@gmail.com',
    description='CLI tool to install and add packages to Django in INSTALLED_APPS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rohan7654/django-include-apps.git',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)

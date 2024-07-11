from setuptools import setup, find_packages

setup(
    name='django-include-apps',    
    version='0.1.1',               
    packages=find_packages(),
    install_requires=[
        'typer',                   
        'requests',
        'inquirer'
    ],
    keywords='django-include-apps django add apps cli ',
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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8',
)

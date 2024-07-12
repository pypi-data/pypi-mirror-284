from setuptools import setup, find_packages
import os

# Read the content of your README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='drfapigenerator',
    version='2.0.1',
    include_package_data=True,
    
    install_requires=[
        'django',
        'djangorestframework',
    ],
    entry_points={
        'console_scripts': [
            # Define any command line scripts here
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 3.2',  # Specify the appropriate Django version
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',

    description="A Django app for automating RESTful API development using Django Rest Framework (DRF), simplifying CRUD operations for Django models.",
    long_description='''DRF API Generator simplifies API development in Django projects by automating the creation of RESTful APIs using Django Rest Framework (DRF). It generates necessary components such as viewsets, serializers, and routing based on your Django models, allowing developers to quickly expose CRUD (Create, Read, Update, Delete) operations via API endpoints. This tool enhances productivity by reducing manual configuration and boilerplate code, making it easier to build and maintain APIs in Django applications.''',
    long_description_content_type='text/plain',
    author='Manoj Kumar Das',
    author_email='manojdas.py@gmail.com',
    url='https://github.com/mddas2/drfapigenerator',
    packages=['drfapigenerator'],
    
)



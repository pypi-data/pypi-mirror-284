from setuptools import setup, find_packages
import os

# Read the content of your README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='drfapigenerator',
    version='1.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.2',
        'djangorestframework',
        'django-filter',
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
    long_description=long_description,
    long_description_content_type='text/markdown',
)

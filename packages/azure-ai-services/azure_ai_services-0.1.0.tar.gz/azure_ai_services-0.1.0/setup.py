# setup.py

from setuptools import setup, find_packages

setup(
    name='azure_ai_services',
    version='0.1.0',
    description='A Python library for Azure AI services with basic and premium features',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mallikarjun',
    author_email='mallikarjun266@gmail.com',
    url='https://github.com/arjun266/azure_ai_services',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

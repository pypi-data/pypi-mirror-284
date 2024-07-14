# setup.py
from setuptools import setup, find_packages

setup(
    name='trsutspidercrypt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'cryptography>=3.0.0',
    ],
    python_requires='>=3.6',
    author='Spidercrypt',
    author_email='votre@email.com',
    description='Une bibliothèque pour le chiffrement AES avec CBC',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mouhawos/spidercryptencrypt',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

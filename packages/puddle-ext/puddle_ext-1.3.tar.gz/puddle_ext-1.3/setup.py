# setup.py
from setuptools import setup, find_packages

setup(
    name='puddle_ext',
    version='1.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'puddle=puddle_ext.cli:main',
        ],
    },
    install_requires=[
        'Pillow',
    ],
)

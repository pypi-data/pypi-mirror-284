# setup.py
from setuptools import setup, find_packages

setup(
    name='puddle_ext',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'puddle=puddle.cli:main',
        ],
    },
    install_requires=[
        'Pillow',
    ],
)

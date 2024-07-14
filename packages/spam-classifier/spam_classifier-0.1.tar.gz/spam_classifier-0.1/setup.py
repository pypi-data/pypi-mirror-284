# setup.py

from setuptools import setup, find_packages

setup(
    name='spam_classifier',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A library for classifying spam messages',
    install_requires=[
        'tensorflow',
        'numpy',
        'pickle',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)

from setuptools import setup, find_packages

setup(
    name='spam_classifier',
    version='0.15',
    packages=find_packages(),
    include_package_data=True,
    description='A library for classifying spam messages',
    install_requires=[
        'tensorflow>=2.0.0',
        'requests',
        'huggingface-hub',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='Non-commercial use only. Contact author for commercial use.',
    Email= 'totoshkus@gmail.com'
)

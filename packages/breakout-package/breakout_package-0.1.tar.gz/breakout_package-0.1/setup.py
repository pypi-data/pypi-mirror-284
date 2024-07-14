# setup.py

from setuptools import setup, find_packages

setup(
    name='breakout_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for breakout strategy calculation.',
    long_description='A package for breakout strategy calculation.',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/breakout_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

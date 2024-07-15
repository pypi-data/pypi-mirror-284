from setuptools import setup, find_packages

setup(
    name='shtcoding',
    version='0.1',
    description='Python functions for controlling Arduino devices',
    author='p00pin0',
    author_email='sht060117@gmail.com',
    packages=find_packages(),
    install_requires=['pyserial'],
)
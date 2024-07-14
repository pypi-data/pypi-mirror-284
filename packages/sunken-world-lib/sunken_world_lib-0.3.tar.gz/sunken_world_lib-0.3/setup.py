import setuptools

from setuptools import find_packages, setup
setup(
    name = 'sunken_world_lib',
    version = '0.3',
    packages=find_packages(),
    py_modules=['sunken_world_lib'],
    install_requires=[],
    package_data={"libs": ["jei-1.20.1-forge-15.4.0.9.jar"]},
)
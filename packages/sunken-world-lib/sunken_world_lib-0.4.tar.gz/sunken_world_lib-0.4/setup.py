import setuptools

from setuptools import find_packages, setup
setup(
    name = 'sunken_world_lib',
    version = '0.4',
    packages=find_packages(),
    install_requires=[],
    package_data={"libs": ["jei-1.20.1-forge-15.4.0.9.jar","skinlayers3d-forge-1.6.6-mc1.20.1.jar"]},
)
from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class CustomInstallCommand(install):
    def run(self):
        print("hello")
        os.system("whoami")   

setup(
    name='iamtestpackage626',
    version='0.1',
    description='A simple demo package',
    packages=find_packages(),
    cmdclass={
        'install': CustomInstallCommand,
    },
)

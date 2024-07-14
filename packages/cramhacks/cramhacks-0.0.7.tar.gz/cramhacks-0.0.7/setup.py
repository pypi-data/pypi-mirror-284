import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class CustomInstallCommand(install):
    def run(self):
        # Run the standard install process
        install.run(self)
        # Execute the bash command and capture the output
        result = subprocess.run(['whoami'], capture_output=True, text=True)
        print(f"User: {result.stdout.strip()}")

setup(
    name='cramhacks',
    version='0.0.7',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)

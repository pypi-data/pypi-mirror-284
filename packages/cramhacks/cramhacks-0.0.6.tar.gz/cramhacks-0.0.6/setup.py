import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        # Run the standard install process
        install.run(self)
        # Execute the bash command and capture the output
        result = subprocess.run(['bash', '-c', 'whoami'], capture_output=True, text=True)
        print(result.stdout)

setup(
    name='cramhacks',
    version='0.0.6',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)

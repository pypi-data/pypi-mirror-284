from setuptools import setup
from setuptools.command.install import install


class InstallCommand(install):
    def run(self):
        raise RuntimeError("You are trying to install a stub package internal-airflow-utils. Maybe you are using the wrong pypi?")


setup(
    name='internal-airflow-utils',
    version='0.0.1',
    author='Egnyte',
    url='https://egnyte.com',
    readme="README.md",
    long_description="""This is a security placeholder package.""",
    long_description_content_type='text/markdown',
    description='A package to prevent Dependency Confusion attacks',
    cmdclass={
        'install': InstallCommand,
    },
)
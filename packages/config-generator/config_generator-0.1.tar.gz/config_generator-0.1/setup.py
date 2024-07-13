from setuptools import setup, find_packages

setup(
    name = 'config_generator',
    version = '0.1',
    packages = find_packages(),
    install_requires = [
        'pydantic>=2.8.2'
    ]
)
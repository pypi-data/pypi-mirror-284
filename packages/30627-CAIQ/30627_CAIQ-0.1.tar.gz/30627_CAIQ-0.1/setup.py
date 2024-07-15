from setuptools import setup, find_packages

setup(
    name='30627_CAIQ',
    version='0.1',
    description='Python functions for controlling Arduino devices',
    author='30627_CAIQ',
    author_email='chaiw06@gmail.com',
    packages=find_packages(),
    install_requires=['pyserial'],
)

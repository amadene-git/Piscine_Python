from setuptools import setup, find_packages

setup(
    name='my_minipack',
    version='0.0.1',
    # url='https://github.com/yourusername/my_minipack',
    author='Your name',
    author_email='your.email@example.com',
    description='A small package containing a logger and a progress function',
    packages=find_packages(where="src"),
    # install_requires=[],
)
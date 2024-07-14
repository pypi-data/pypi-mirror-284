from setuptools import setup, find_packages

setup(
    name='sheetconnect',
    version='1.0.2',
    description='Simple get data from Google sheet in form of Pandas dataframe',
    author='Pongsakorn Nimphaya',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
)
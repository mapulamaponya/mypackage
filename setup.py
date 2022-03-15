from setuptools import setup, find_packages

setup(
    name= "mypackage",
    version="0.1",
    packages=find_packages(exclude=["tests"]),
    license= 'MIT',
    description= "EDSA example python package",
    long_description=open('ReadMe.md').read(),
    install_requires=["numpy"],
    url='http://github.com/<username>/<package-name>',
    author="<Your Name>",
    author_email="<Your Email"
)
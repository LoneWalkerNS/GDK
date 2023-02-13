from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Package for Updating All Python Packages'
LONG_DESCRIPTION = 'A package that makes it easy to update all python packages and classifies the packages on basis of updated & not updated.'

setup(
    name="GDK",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Lone Walker",
    author_email="lonewalkerns@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='pip',
    classifiers= [
        "Development Status :: 1 - A",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
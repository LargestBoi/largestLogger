#Importing the library used to setup the package via a pip install
import setuptools
#Just the simple data about the library
setuptools.setup(
    name="largestLogger",
    version="1.1.1",
    author="LargestBoi",
    description="A simple, open source logging library. It can be easily added to a program and provides a colourful, reliable and managed logging system to your application/script! https://github.com/LargestBoi/largestLogger",
    packages=["largestLogger"],
    install_requires=['datetime', 'colorama'],
)
#Importing the lib used to setup the package via a pip install
import setuptools
#Just the simple data about the lib
setuptools.setup(
    name="LargestLogger",
    version="0.0.5",
    author="LargestBoi",
    description="A simple, open source logging library. It can be easily added to a program and provides a colourful, reliable and managed logging system to your application/script!",
    packages=["LargestLogger"],
    install_requires=['datetime', 'colorama'],
)
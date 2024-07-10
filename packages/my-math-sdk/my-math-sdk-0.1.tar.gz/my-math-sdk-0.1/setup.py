# setup.py

from setuptools import setup, find_packages

setup(
    name="my-math-sdk",
    version="0.1",  
    packages=find_packages(),
    description="A simple math operations SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="KODELA PRASANNA LAXMI",
    author_email="prasannalaxmi175@gmail.com",
    url="https://github.com/prasannalaxmi200/samplesdk",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

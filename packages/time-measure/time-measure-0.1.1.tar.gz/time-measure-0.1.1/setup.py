from setuptools import setup, find_packages

setup(
    name="time-measure",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Thibault Castells",
    author_email="thib.castells@icloud.com",
    description="Various tools to easily measure elapsed time in python (with function wrapper, context manager, or decorator).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ThibaultCastells/time_measure",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
# setup.py

from setuptools import setup, find_packages

setup(
    name="flex_ai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        # e.g., 'requests', 'numpy',
    ],
    author="Ariel Cohen",
    author_email="ariel042cohen@gmail.com",
    description="Flex AI client library",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arielcohen4/flex_ai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

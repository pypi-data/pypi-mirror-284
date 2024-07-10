from setuptools import setup, find_packages

setup(
    name="simplify5d",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    author="James Carruthers",
    author_email="your.email@example.com",
    description="A module for simplifying 2D and 3D lines using Ramer-Douglas-Peucker algorithm",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jamescarruthers/simplify5d",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
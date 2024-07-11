from setuptools import setup, find_packages

setup(
    name="gpctools",
    version="0.1.8",
    author="Danilo B. M. de Lima",
    author_email="d.lima@gp-joule.de",
    description="Python package for common use tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/danbarml/gpctools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)

""" Setup """
from pip._internal.req import parse_requirements, PipSession
from setuptools import setup, find_packages

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(filename='requirements.txt', session=PipSession())
install_reqs_dev = parse_requirements(filename='requirements_dev.txt', session=PipSession())

# reqs is a list of requirements.txt
# reqs_dev is a list of requirements_dev.txt
reqs = install_reqs
reqs_dev = install_reqs_dev

with open(file="README.md", mode="r", encoding="UTF-8") as fh:
    long_description = fh.read()

setup(
    name="jf-chess",
    version="0.0.0",
    author="Justin Freels",
    author_email="justin@justinfreels.com",
    description="Python library to interact with Chess.com API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jfreels",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        reqs,
        reqs_dev
    ],
    extras_require={
        "dev": [
            "setuptools",
            # "twine",
            # "wheel",
            "python-dotenv"
        ]
    },
    python_requires='>=3.6',
)

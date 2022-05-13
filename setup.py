""" Setup """
import pathlib

import pkg_resources
from setuptools import setup, find_packages

with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires = [
        str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

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
    install_requires=install_requires,
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

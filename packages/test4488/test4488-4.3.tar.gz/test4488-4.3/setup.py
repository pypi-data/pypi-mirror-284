import re

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

from aider import __version__

packages = find_packages(exclude=["benchmark"]) + ["aider.website"]

setup(
    name="test4488",
    description="AI Senior Software Engineer",
    version=__version__,
    packages=packages,
    include_package_data=False,
    install_requires=requirements,
    python_requires=">=3.9,<3.13",
    entry_points={
        "console_scripts": [
            "tenten = aider.main:main",
        ],
    },
)

from pathlib import Path

from setuptools import find_packages, setup

VERSION = "0.1.0"
DESCRIPTION = "More useful version of du"
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="du_v2",
    version=VERSION,
    author="Tyler Lum",
    author_email="tylergwlum@gmail.com",
    url="https://github.com/tylerlum/du_v2",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["tyro", "tqdm"],
    keywords=[],
    entry_points={
        "console_scripts": [
            "du_v2=du_v2.du_v2:main",
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)

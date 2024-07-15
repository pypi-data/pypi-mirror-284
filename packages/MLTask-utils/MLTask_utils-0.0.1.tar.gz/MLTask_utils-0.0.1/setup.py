from setuptools import setup, find_packages


VERSION = "0.0.1"
DESCRIPTION = "TBD"
LONG_DESCRIPTION = "TBD"

# Setting up
setup(
    name="MLTask_utils",
    version=VERSION,
    author="Mister Joessef",
    author_email="<misterjoessef@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[
        "mltask",
    ],
)

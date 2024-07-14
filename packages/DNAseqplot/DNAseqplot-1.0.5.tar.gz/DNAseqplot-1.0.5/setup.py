from setuptools import setup
from setuptools import find_packages

version_py = "DNAseqplot/_version.py"
exec(open(version_py).read())

setup(
    name="DNAseqplot", # Replace with your own username
    version=__version__,
    author="Benxia Hu",
    author_email="hubenxia@gmail.com",
    description="plot multiple DNA sequences with point mutations",
    long_description="plot multiple DNA sequences with point mutations",
    url="https://pypi.org/project/DNAseqplot/",
    entry_points = {
        "console_scripts": ['DNAseqplot = DNAseqplot:main',]
        },
    python_requires = '>=3.6',
    packages = ['DNAseqplot'],
    install_requires = [
        'pandas',
        'argparse',
        'matplotlib',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe = False,
  )
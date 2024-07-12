from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='b15py',
    version='1.0.0.1',
    packages=find_packages(),
    package_data={'b15py': ['b15py.so']},
)


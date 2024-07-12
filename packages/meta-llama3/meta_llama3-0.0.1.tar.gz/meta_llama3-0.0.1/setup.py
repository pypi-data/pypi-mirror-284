from pathlib import Path
from setuptools import find_packages, setup

def get_requirements(path: str):
    return [l.strip() for l in open(path)]

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="meta_llama3",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    long_description=long_description,
    long_description_content_type='text/markdown',
)
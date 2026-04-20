from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='mlproject1',
    version='0.0.1',
    author='Nidhi',
    author_email='nidhiy2810@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
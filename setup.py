from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    
    # This function reads the requirements from a file and returns them as a list.
    
    with open(file_path) as file:
        requirements = file.readlines()
        requirements= [req.replace('\n', '') for req in requirements]
    
    
    requirements = []
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlpractice',
    version='0.1.0',
    author='Jirtus',
    author_email='jirtussanasam@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),
)
from setuptools import find_packages,setup
from typing import List;

HYPEN_E = "-e ."

def get_requirements(file_path:str)->list[str]:
    '''this funcation return the requirements of libraries'''
    requirements = [];
    with open(file_path) as fo:
        requirements = fo.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    
    return requirements;
setup(
    name='mlproject',
    version="0.0.1",
    author='Yash',
    author_email='yashbadgujarofficial@gmai.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
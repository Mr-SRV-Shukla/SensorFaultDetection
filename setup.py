from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)-> List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n",'') for req in requirements]
        #  -e . , will not install from setup.py 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    # Name of the Package
    name='SensorFaultDetection',
    # version of the packages
    version='0.0.1',
    # Author of the packages
    author='Sourav Shukla',
    # Author E-mail 
    author_email='souravshukla985@gmail.com',
    # all requirement for the package 
    install_requires=get_requirements('requirements.txt'),
    # package should read all the modules from the project
    packages=find_packages()
    )
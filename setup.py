from setuptools import find_packages,setup
from typing import List

hyphen_const = '-e .'
def get_requirements(file_path:str) ->List[str]:
    '''
    This function returns the list of requirements from the given file.
    It removes the '-e .' entry if present.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if hyphen_const in requirements:
            requirements.remove(hyphen_const)

    return requirements

setup(
name = 'MLProject', 
version = '0.0.1',
author = 'Sauvik',
author_email='sauvikg08@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
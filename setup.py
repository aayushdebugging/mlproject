from setuptools import find_packages, setup
from typing import List



HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    Read requirements file and return list of requirements
    '''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
           
    
setup(
name='mlproject',
version='00.1',
author='Aayush',
author_email='22it3001@rgipt.ac.in',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
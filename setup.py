from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    this will get the requirements
    '''

    requirements=[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Naman',
    author_email='2004naman7461@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    
)
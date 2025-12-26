from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirements"""""
    requirements=[]
    with open(file_path,'r') as file_obj:       # Open the requirements file
        requirements=file_obj.readlines()   # Read all lines from the file
        requirements=[req.replace('\n','') for req in requirements] # Remove newline characters from each line
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # Remove '-e .' if present
    return requirements


## Metadata about the package
setup(
    name='mlproject',
    version='0.1.0',
    author='Anas Saifi',
    author_email='anassaifi8912@gmail.com',
    packages=find_packages(), # Automatically find packages in the directory by finding __init__.py files
    install_requires=get_requirements('requirements.txt'), # install dependencies from requirements.txt


)

from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    """This Function Will Return The List Of requirements.txt"""
    requirements = []
    with open(file_path) as fp:
        requirements = fp.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(

    name = "ML Project",
    version = "0.0.1",
    author = "Chandan",
    author_email = "gangaputrachandan@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
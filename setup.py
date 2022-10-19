from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This functions will return list of requirement_list
    """
    requirement_list:List[str] = []
    return requirement_list
    

setup(

    name="sensor",
    version="0.0.1",
    author="Deepak Kumar",
    author_email="ideepak1608@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements() #["pymongo==4.2.0"]
)
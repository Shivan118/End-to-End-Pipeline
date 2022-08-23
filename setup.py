from setuptools import setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
#REMOVE_PACKAGE = "-e ."


def get_requirement_list()->List[str]:
    """
    Description: Thisw function is goging to return list of requirement
    mention in requirements.txt

    return This function is goging to return a list which conatin name of libraries 
    mentioned in requirements.txt file
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
# Declearing Variables for Setup Functions

setup(
    name="Housing price prediction",
    license="Apache",
    version="0.0.1",
    description="Project has been completed.",
    author="Shivan Kumar",
    packages=["housing"],
    install_requires=get_requirement_list()
)

#if __name__ == "__main__":
 #   print(get_requirement_list())
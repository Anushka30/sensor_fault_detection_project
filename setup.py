from setuptools import find_packages, setup
from typing import List


def get_requirements():
    """
    This function will return list of requirements
    :return:
    """
    # requirement_list: List[str] = []
    with open("requirements.txt") as f:
        requirement_list = f.read().splitlines()

    return requirement_list


# python setup.py install
#
setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="anushka30j@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),  # ["pymongo==4.2.0"]
)

if __name__ == "__main__":
    get_requirements()